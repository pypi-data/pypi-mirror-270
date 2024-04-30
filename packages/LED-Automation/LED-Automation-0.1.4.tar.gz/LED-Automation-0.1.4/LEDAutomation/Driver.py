from enum import Enum
from Hal import HAL
from time import sleep
# Requires PyFTDI to be installed on the device and the FTDI device to be plugged in

# Scripts in the Scripts folder for finding connected i2C devices
# py .venv/Scripts/i2cscan.py


# Board won't be changing, so having items for the , pinout might change for the console buttons etc, so make sure those are provided via a map or something.
# goal is just to toggle buttons


# General Notes on code:
# a 1 bit is considered HIGH/UP/ACTIVE and a 0 bit is considered LOW/DOWN/INACTIVE in relation to documentation and schematics
# Register addresses are found in the documentation for the device that is controlling the LED's: in our case the PCA9506 chip
# Which pins on the chip that need to be used to toggle the LED's is located on the schematic for the board. This also shows which IO bank on the chip has the LED pins (IO_4 aka bank 4)

#General Flow:

# init the device
# toggle the pins you want to write to to output mode, this uses the config register for the pins.
# write to the output register for the pins. Each write will update the pins and update the device automatically
     
# use this to interact with I2C devices
class myFTDI:
    """TODO Deprecate use the driver instead combined with the HAL"""

    def __init__(self, address = "ftdi://::1/", interface:int = 1):

        # Interface 1 is I2C to the GPIO Expanders
        if(interface == 1):
            # init PyFTDI I2C controller for the specified interface aka group of 8 pins on the FTDI chip
            # Note This is all self contained in the expanders class now.
            assert True


        # Interface 2 is SPI and connects to J107. Use the SPI communication protocol of PyFTDI to interact
        elif(interface == 2):
            self.newVar = False
            assert True
        
        # Interface 3 contains the pins for the USB hub I2c in a non standard pinout. This means we use the pyftdi.gpio library and manually implement the I2C protocol using it.
        elif(interface == 3):
            assert True
        
        # Interface 4 is manual and has the pins that control the thumbdrives. use the pyftdi.gpio library to manually interact with the pins.
        elif( interface == 4):
            assert True
        
        else:
            assert False, "Interface number was not a valid interface value; Valid 1-4 Yours: " + str(interface)


class Driver:
    """ Driver class that will be used in the Test classes. Should use the lower level HAL methods to do more advanced things. Only 1 instance of this should be used at a time."""

    _instance = None # Only have 1 instance that is used across all drivers. aka make this a Singleton class.

    def __init__(self, consoleType, isTM):
        """ Pass in the list of items on the GPIO to setup their config"""
        self.__hal = HAL(consoleType, isTM) # Creates its own i2c connection and manages it itself
        print("Driver Is Ready")

    def __new__(cls, *args, **kwargs):
        """ make all objects have the same  """
        cls._instance = object.__new__(cls)
        return cls._instance

    def toggleLED(self, led:Enum, on:bool):
        """ Toggle a given LED on or off """
        self.__hal.toggleLED(led, on)
        
    def pressButton(self, button:Enum, seconds = .1, times = 1):
        """ press a given button. Pass in Seconds to determine how long to press for, (0.1s default aka a tap), times is how many times to press it"""
        assert seconds >= .1, f"Minimum button press length is 0.1 seconds."
        for i in range(0, times):
            self.__hal.toggleButton(button, True)
            sleep(seconds)
            self.__hal.toggleButton(button, False)
            sleep(.5)
            print("Pressed:", button.name)

    def pressTwoButtons(self, button:Enum, button2:Enum, seconds = .1):
        """Press 2 buttons at the same time. Technically, it will start holding button before button 2, wait the given amount of time, then release button before button 2"""
        assert seconds >= .1, f"Minimum button press length is 0.1 seconds."
        self.__hal.toggleButton(button,True)
        self.__hal.toggleButton(button2,True)
        sleep(seconds)
        self.__hal.toggleButton(button,False)
        self.__hal.toggleButton(button2,False)
        sleep(.5)
        print("Pressed:", button.name, "and", button2.name)
