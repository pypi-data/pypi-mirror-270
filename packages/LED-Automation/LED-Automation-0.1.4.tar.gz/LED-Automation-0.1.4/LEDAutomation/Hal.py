from Connections import ConsoleType
from PLedConsole import PLEDConnections
from LedConsole import LEDConnections, LEDConnectionsTM
from enum import Enum
from Expanders import Expanders
"""
    This file is meant to contain higher level interactions with the hardware and manages the hardware connections.

"""

class HAL:
    """Stores the connections on the board and interfaces with all aspects of the Hardware"""
    def __init__(self, console:ConsoleType, isTM:bool): # pass in the console type?
        """Create an instance of this class, which handles the hardware interface. Pass in an instance of the mapping between connection points and buttons etc."""
        if console is ConsoleType.PLED: # PLED Has no real differences in connections between frame types
            self.__expanders = Expanders(PLEDConnections()) # Connection to the expanders
        elif isTM: # Assumes it's an LED from here on.
            self.__expanders = Expanders(LEDConnectionsTM())
        else:
            self.__expanders = Expanders(LEDConnections)

    def toggleButton(self, button:Enum, on:bool):
        """ Toggle a button to be on or off """
        # Buttons need to be pulled low to be in the pressed state.
        self.__expanders.writeExpanderOutput(button, not on) 

    def toggleLED(self, led:Enum, on:bool):
        """ Toggle an LED to be on or off """
        self.__expanders.writeExpanderOutput(led, on)