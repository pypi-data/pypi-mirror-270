from abc import ABC
from enum import Enum, auto
#List out the valid connections here as an enum. Use this enum in the code to map pins to this.

"""File that contains the hard coded connections on the board itself and an interface to map connections to human readable Enums. Extend the Connections class and fill in your own mapping of Data/Scan lines for the given connection."""
class ConsoleType(Enum):
    PLED = auto()
    LED = auto()


class LEDS(Enum):
        """The name of the LED's that are togglable on the automation board"""
        ONE = auto()
        TWO = auto()
        THREE = auto()
        FOUR = auto()

# Use this enum to fill out the 2d arrays which map connection points to buttons
class Buttons(Enum):
    """ All the Buttons for the PLED/LED Consoles that are available to use 
        A Subset of what can be found here: (Ignores Group Training LED console keys)
        PLED-> https://bitbucket.org/johnsonhealthtech/raven_io_gd32f305ve/src/master/Modules/Key_Lib/keyboard.h
        LED -> https://bitbucket.org/johnsonhealthtech/io_vulcan/src/master/UCB/src/Key/keyboard144.h
    """
    # KB_KEY_NONE = None
    
    # TV control keypad
    TV_POWER = auto()
    TV_LAST = auto()
    TV_ENTER = auto()
    TV_DASH = auto()
    TV_MUTE = auto()
    TV_CHANUP = auto()
    TV_VOLUP = auto()
    TV_CHANDOWN = auto()
    TV_VOLDOWN = auto()
    TV_0 = auto()
    TV_1  = auto()
    TV_2 = auto()
    TV_3  = auto()
    TV_4 = auto()
    TV_5 = auto()
    TV_6 = auto()
    TV_7 = auto()
    TV_8 = auto()
    TV_9 = auto()

    # lower area misc. keys
    KB_INCLINE_RES_DOWN = auto()
    KB_INCLINE_RES_UP = auto()
    KB_SPEED_RES_UP = auto()
    KB_SPEED_RES_DOWN = auto()
    KB_STOP = auto() # K_BACK
    KB_PAUSE = auto()
    KB_RUN = auto()   # K_ENTER
    KB_CONCIERGE = auto()

    # Lower area Keypad
    KB_DELETE = auto()
    KB_ENTER = auto()
    KB_0 = auto()
    KB_1 = auto()
    KB_2 = auto()
    KB_3 = auto()
    KB_4 = auto()
    KB_5 = auto()
    KB_6 = auto()
    KB_7 = auto()
    KB_8 = auto()
    KB_9 = auto()

    # LED Upper board keys
    K_LEFT_DISPLAY_SELECT = auto()
    K_RIGHT_DISPLAY_SELECT= auto()
    K_MANUAL = auto()
    K_CONSTANT_WATTS = auto()
    K_TARGET_HR = auto()
    K_ROLLING_HILLS = auto()
    K_FAT_BURN = auto()
    K_FITNESS_TEST = auto()
    K_CHECKMARK = auto()
    K_MINUS = auto()
    K_PLUS = auto()
    K_TIME_MODE = auto()

    #LED MIST Others
    K_Q_INCLINE_RES_UP = auto()
    K_Q_INCLINE_RES_DOWN = auto()
    K_Q_SPEED_RES_UP = auto()
    K_Q_SPEED_RES_DOWN = auto()
    K_Q_STOP = auto()
    K_Q_GO = auto()
    K_Q_PAUSE = auto()

    # PLED Upper Board Keys
    K_FAN = auto()
    ATM_RIGHT_1 = auto()
    ATM_RIGHT_2 = auto()
    ATM_RIGHT_3 = auto()
    ATM_RIGHT_4 = auto()
    ATM_LEFT_1 = auto()
    ATM_LEFT_2 = auto()
    ATM_LEFT_3 = auto()
    ATM_LEFT_4 = auto()


class Connections(ABC):
    """ One D array that follows the mapping in the cyclops and Vulcan codebase. X axis is Data line, Y axis is Scan line. Format it just like the code in the LED/PLED codebase.
         Reference: Should be able to easily use this code to create button mappings - Buttons to Data/Scan Lines: (PLED, Vulcan)
         https://bitbucket.org/johnsonhealthtech/raven_io_gd32f305ve/src/master/Modules/Key_Lib/Keyboard.c
         https://bitbucket.org/johnsonhealthtech/io_vulcan/src/master/UCB/src/Key/KeyPad_Table144.h 
         
        Example usage of this Interface
        Use the Buttons class to fill in the data and scan lines. Use the value [None] for entries that don't map to anything.

        class PLEDConnections(Connections):
            J200 = [ # Data 11                        12             13                    14                15
                Buttons.TV_LAST, 	          Buttons.TV_MUTE,     Buttons.TV_3, 	     Buttons.TV_2, 	    Buttons.TV_1,	     # Scan 15
                Buttons.TV_POWER,             None,		           Buttons.TV_6, 	     Buttons.TV_5, 	    Buttons.TV_4,	     # Scan 16
                Buttons.TV_CHANUP, 	          Buttons.TV_VOLUP,    Buttons.TV_9, 	     Buttons.TV_8, 	    Buttons.TV_7,	     # Scan 17
                Buttons.TV_CHANDOWN, 	      Buttons.TV_VOLDOWN,  Buttons.TV_ENTER,     Buttons.TV_0, 	    Buttons.TV_DASH,     # Scan 18
                Buttons.K_Q_INCLINE_RES_DOWN, None,                None,                 None,              None,                # Green
                Buttons.K_Q_SPEED_RES_DOWN,   Buttons.K_Q_PAUSE,   Buttons.K_Q_STOP,      None,              None,                # RED
            ] 
    """

    J200: list[Enum] = None
    """ D11-15 x S15 - 18, Green, Red """
    J201: list[Enum]  = None
    """ D11 - D15 x S11 - 14, Green """
    J202: list[Enum]  = None
    """ D16-19 x S17"""
    J203: list[Enum] = None
    """ D16-19 x S15"""
    J204: list[Enum] = None
    """ EstopA 1, EstopB 2, Estop SW A 3, Estop SW B 4"""
    leds: list[Enum] = [LEDS.ONE, LEDS.TWO, LEDS.THREE, LEDS.FOUR]
    """Leds on the Tester Board D200-203"""

    def __init__(self):
        """Verify that the overrides are formatted correctly."""
        if self.J200 is not None:
            assert len(self.J200) == 30, "Make sure all the data and scanlines have a value or None in the Connections grid for J200"
        if self.J201 is not None:
            assert len(self.J201) == 25, "Make sure all the data and scanlines have a value or None in the Connections grid for J201"
        if self.J202 is not None:
            assert len(self.J202) == 4, "Make sure all the data and scanlines have a value or None in the Connections grid for J202"
        if self.J203 is not None:
            assert len(self.J203) == 4, "Make sure all the data and scanlines have a value or None in the Connections grid for J203"
        if self.J204 is not None:
            assert len(self.J204) == 4, "Make sure all the data and scanlines have a value or None in the Connections grid for J204"
        if self.leds is not None:
            assert len(self.leds) == 4, "Make sure all the data and scanlines have a value or None in the Connections grid for the LEDS"
