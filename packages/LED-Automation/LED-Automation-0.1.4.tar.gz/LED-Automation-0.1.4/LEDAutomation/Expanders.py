import sys
from enum import IntFlag
from  pyftdi.i2c import I2cPort
from pyftdi import i2c
from Connections import Connections
from enum import Enum

class ExpanderGPIOAddress:
    """ This class stores the address for a pin: the GPIO expander it is on, the bank number, and the pin number. Also stores whether it should be input or output"""
    def __init__(self, expander:int, bank:int, pin:int, output:bool = True):
        """ A class to store information important for things connected to the GPIO Expanders
            Args:
                expander(int): Expander that this relates to -> 0 or 1 (0 == U200, 1 == U201)
                bank(int): Which bank the pin is on -> 0 through and including 4
                pin(int): The pin number in the bank -> 0 through and including 7
                output(bool): whether the pin should be output/write to or input/read from mode
        """
        self.__validateExpander(expander)
        self.__validateBank(bank)
        self.__validatePin(pin)
        self.expander = expander
        self.bank = bank
        self.pin = pin
        self.output = output
    def __validateExpander(self,expander):
        """ Make sure the expander number is either 0 or 1 """
        assert expander == 0 or expander == 1
    def __validateBank(self, bank):
        """ Make sure the bank number is valid and within range (0 - 4)"""
        assert bank >= 0 and bank <= 4
    def __validatePin(self, pin):
        """ Make sure the bit is within a byte aka 0 through and including 7"""
        assert pin >= 0 and pin <= 7
    def __str__(self) -> str:
        return f"Ex: {self.expander} Bank: {self.bank} Pin: {self.pin} IsOutput: {self.output}"
    
class PCA9506:
    """This class controlls all the interactions with a GPIO Expander. Chaches wherever possible, so if the board ever disconnects from the pc, the scripts will need to restart."""
    __connection = None # The port that gets opened by the i2c controller. Use this to call the normal FTDI methods
    __configCache = dict() # Cache tracking the config state for things that have been edited. stores the byte config for each bank. Updates whenever a config changes {bankNum: byte}
    __outputBankCache = dict() # Cache showing the changes last seen. Stores the byte data that was last written for each bank. Updates anytime something is written  {bankNum: byte}

    # Enum of registers that are available to write to
    class PCAREG(IntFlag):
        IREG = 0x00 # Input Register
        OREG = 0x08 # Output Register
        PINT = 0x10 # Perform Interrupt Register
        IOCONFIG = 0x18 # IO Configuration Register
        MINT = 0x20 # Mask Interrupt Register

    def __init__(self, i2CConnection: I2cPort):
        """ Pass in the connection to the i2c line"""
        # store the connection so it can be used for other methods in the class
        self.__connection = i2CConnection

    # Core functions

    def __isValidBank(self,bank):
        """ Checks that the given bank number is valid, there are 5 banks labelled 0 through and including 4 """
        assert bank >= 0 and bank <=4

    def __writeToReg(self, address, bits:int):
        """Uses the pyftid write_to method
        Writes the bits to the specified address.

        Args:
            address (int): Hex address of the register to write to
            bits (int): The bits that we are writing
        """
        
        converted = bits.to_bytes(1, sys.byteorder)
        #print("Writing to:", hex(address), "with value:",converted)
        self.__connection.write_to(address, converted)
    
    def __readReg(self, address) -> int:
        """Reads the current bits of the target register"""
        return int.from_bytes(self.__connection.read_from(address, 1), sys.byteorder)

    def __readPreviousOutput(self, bank: int) -> int:
        """Read in the previous byte that was output to the bank"""
        # TODO Optimize reading in previous state, to prevent having to directly read it in from the board every time?. Maybe cache the previous state when it is written or smth
        self.__isValidBank(bank)
        return self.__readReg(bank | self.PCAREG.OREG)

    def __readConfig(self, bank: int) -> int:
        # TODO Optimize reading in previous state, to prevent having to directly read it in from the board every time?. Maybe cache the previous state when it is written or smth
        self.__isValidBank(bank)
        return self.__readReg(bank | self.PCAREG.IOCONFIG)

    def __writeToConfig(self, bank:int, bits):
        """ Write to the config register for a bank of bits

        Args:
            bank (int): which bank to write to
            bits (bytearray): what values the bits aka pins should take
        """
        self.__isValidBank(bank)
        self.__writeToReg(bank | self.PCAREG.IOCONFIG, bits)

    def __writeToOutput(self, bank:int, bits):
        """ Write to the output for a bank
        Assumes that output is enabled already
        Args:
            bank (int): which bank to write to
            bits (bytearray): what values the bits aka pins should take
        """
        self.__isValidBank(bank)
        self.__writeToReg(bank | self.PCAREG.OREG, bits)
    
    def __modifyBit(self, byte:int, targetBit: int, on:bool) -> int:
        """ Modify the target bit's value to either on or off in the given byte. Does not modify the other bits"""
        if(on):
            return byte | (1 << targetBit)
        else:
            return byte & (~ (0x01 << targetBit) )  # set the target bit to 1 and then invert the bits so target is a 0 and all others are Ones. Then and with the given byte

    def __writeToConfigPin(self, location:ExpanderGPIOAddress, setIsOutput:bool):
        """ Set a given pin to be output or input. Call this before writing to any pins or reading from a Read Register. Caches previous state and only writes to it if it changed.
            Args:
                setIsOutput (bool): set the pin to input(False)  or output (True)
        """

        #print("Write Config")
        
        # Read from the board if the config is not in the cache
        if location.bank not in self.__configCache.keys():
            self.__configCache[location.bank] = self.__readConfig(location.bank)
        
        config = self.__configCache[location.bank]
        
        #print(bin(config))
        newConf = self.__modifyBit(config,location.pin, not setIsOutput)

        # Ignore writing if there is no change
        if newConf == config:
            return

        #print(bin(newConf))
        self.__configCache[location.bank] = newConf # Write to cache
        self.__writeToConfig(location.bank, newConf) # 0 is output

        if location.bank in self.__outputBankCache.keys():
            del self.__outputBankCache[location.bank] # Invalidate the output cache for the bank since with a config change, it might have junk in it.

    # Public facing functions
        
    def writeToOutputPin(self, location:ExpanderGPIOAddress, value:bool):
        """ Write a value (True == 1, False == 0) to the given output pin"""
        # make sure the pin is set to output before writing to it. Ok to call each time since it works based on a cache, so it will only run if there are changes.
        self.__writeToConfigPin(location, True)

        # Grab from cache if it has been not been used before
        if location.bank not in self.__outputBankCache.keys():
            self.__outputBankCache[location.bank] = self.__readPreviousOutput(location.bank)

        #print("Write to Output")
            
        oldState = self.__outputBankCache[location.bank] # Read bits for the bank from the cache
        #print("Old Pin State",bin(oldState))
        newState = self.__modifyBit(oldState,location.pin, value)
        #print("New Pin State",bin(newState))
        self.__outputBankCache[location.bank] = newState # Write to cache
        self.__writeToOutput(location.bank, newState)

"""Handle the interaction with the GPIO expanders"""

class Expanders:
    """This class handles the connection and interaction with the multiple expanders that are on the board"""
    def __init__(self, connections:Connections):
        """Init a connection to the GPIO Expanders. Provide the mapping of connection points to items.
        Args:
            connections (Connections): Class that extends the Connections Class that fills in the mappings for the interfaces fields
        """
        self.__i2cController = i2c.I2cController()
        try:
            self.__i2cController.configure("ftdi://::1/" + "1") # Uses the first interface since it is dedicated to the expanders.
        except Exception as err:
            print("\nCould not connect to Automation Board. Please make sure it is plugged in and has power.")
            raise err
        
        #Init devices connected to I2C line
        self.PCA9506_A = PCA9506(self.__i2cController.get_port(0x21)) # I2C Address 0x24
        self.PCA9506_B = PCA9506(self.__i2cController.get_port(0x22)) # I2C Address 0x22
        self.__pinMapping = self.__convertConnectionsToMapping(connections)
        #print(self.__pinMapping)

    def writeExpanderOutput(self, item:Enum, value:bool):
        """Write a value to an item on the board. True is on, False is off
            Args:
                item(Enum): Enum value for an item that is connected to the board.
                value(bool): value to write, either True(1) or False(0)
        """
        location = self.__pinMapping.get(item)
        
        assert location != None, f"Could not find a mapping of {item.name} to an Expander location. Please check your Connection Arrays to make sure they have the item in it"
        #print(f"Item: {item} Location: {location} Toggle: {value}")
        if(location.expander == 0):
            return self.PCA9506_A.writeToOutputPin(location, value)
        else:
            return self.PCA9506_B.writeToOutputPin(location, value)

    def __convertConnectionsToMapping(self, con:Connections) -> dict[Enum, ExpanderGPIOAddress]:
        newMap:dict[Enum, ExpanderGPIOAddress] = {}
        newMap.update(self.__optoMapping(con.J200, False, 0))
        newMap.update(self.__optoMapping(con.J201, True, 0))
        newMap.update(self.__optoMapping(con.J202, True, 20)) # 21st bit on the right side of the 2 optoplexers.
        newMap.update(self.__optoMapping(con.J203, True, 24)) # 25th pin is where it starts
        newMap.update(self.__optoMapping(con.J204, True, 28)) # the 29th pin is where it starts
        newMap.update(self.__optoMapping(con.leds, False, 41)) # the 41st pin is where it starts
        return newMap

    def __optoMapping(self, itemList:list[Enum], isRightSide: bool, offsetBitCountOnTheSide:int = 0)-> dict[Enum, ExpanderGPIOAddress]:
        """ Get the map of the optocoupler inputs to pin io on the expander. Pass in whether the lines are on the right or left side. Only 1 side is allowed at a time.
            Can pass in an offset, so how far off from the 0'th position on the given side of the expander the start pin is for the connected device.
            Works off the assumption that for a given list of items, they are connected to adjacent pins on the side of an expander.
        """
        outDict:dict[Enum, ExpanderGPIOAddress] = {}
        if itemList == None: return outDict
        
        for inputNum in range(0,len(itemList)):
            item:Enum = itemList[inputNum]
            if item == None:
                #print(f"Opto Input: {inputNum} -> None")
                continue

            #print(f"Opto Input {"Right" if isRightSide else "Left"}: {inputNum + offsetBitCountOnTheSide} -> {item.name}")
            # Get the expander, bank, and pin num based on the Optoplexer mapping

            if isRightSide:
                # get bytes, then mod by 2 to get whether it is the first or 2nd bank on the given expander. Times 2 to skip numbers. Offset by 1 since right side is 1 indexed.
                ioBank = (((inputNum + offsetBitCountOnTheSide) // 8) % 2) * 2 + 1
                expander = 0 if (inputNum + offsetBitCountOnTheSide) < 16 else 1 
            else:
                # get bytes, then mod by 2 to get whether it is the first or 2nd bank on the given expander. Times 2 to skip numbers. Offset by 1 since right side is 1 indexed.
                ioBank = (((inputNum + offsetBitCountOnTheSide) // 8) % 3) * 2
                expander = 0 if (inputNum + offsetBitCountOnTheSide) < 24 else 1 

            pin = (inputNum + offsetBitCountOnTheSide) % 8
            
            # Save the map of the button to the pin on the expander.
            addr = ExpanderGPIOAddress(expander, ioBank, pin)
            #print(f"{item.name:<20} index: {inputNum:<6} -> {str(addr):<6}")
            if item in outDict.keys():
                print(f"{item.name} exists already at location {outDict[item]}, Overwritting with: {addr}")
            outDict[item] = addr
        
        return outDict     