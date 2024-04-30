from Connections import Connections, Buttons

# Mappings sourced from:
# https://bitbucket.org/johnsonhealthtech/io_vulcan/src/master/UCB/src/Key/KeyPad_Table144.h

class LEDConnections(Connections):
    """The map of items to connection points to pass to the Driver when it is setup. This supports All LED frame types. It does not support LED Group Training."""
    J200 = [ # Data 11                        12             13                    14                15
        Buttons.TV_LAST, 	          Buttons.TV_MUTE,     Buttons.TV_3, 	     Buttons.TV_2, 	    Buttons.TV_1,	     # Scan 15
        Buttons.TV_POWER,             None,		           Buttons.TV_6, 	     Buttons.TV_5, 	    Buttons.TV_4,	     # Scan 16
        Buttons.TV_CHANUP, 	          Buttons.TV_VOLUP,    Buttons.TV_9, 	     Buttons.TV_8, 	    Buttons.TV_7,	     # Scan 17
        Buttons.TV_CHANDOWN, 	      Buttons.TV_VOLDOWN,  Buttons.TV_ENTER,     Buttons.TV_0, 	    Buttons.TV_DASH,     # Scan 18
        Buttons.K_Q_INCLINE_RES_DOWN, None,                None,                 None,              None,                # Green
        Buttons.K_Q_SPEED_RES_DOWN,   Buttons.K_Q_PAUSE,   Buttons.K_Q_STOP,     None,              None,                # RED
    ]                               # TODO Treadmill USES D12,RED -> Buttons.K_Q_STOP and D13,RED -> Buttons.K_Q_GO

    J201 = [ # Data 11                  12                      13                      14                      15
        Buttons.KB_INCLINE_RES_DOWN, Buttons.KB_1,              Buttons.KB_2,   Buttons.KB_3,         Buttons.KB_SPEED_RES_UP,     # Scan 11
        Buttons.KB_INCLINE_RES_UP,   Buttons.KB_STOP,           Buttons.KB_4,   Buttons.KB_5,         Buttons.KB_6,                # Scan 12
        Buttons.KB_RUN,              Buttons.KB_7,              Buttons.KB_8,   Buttons.KB_9,         Buttons.KB_CONCIERGE,        # Scan 13
        Buttons.KB_PAUSE,            Buttons.KB_DELETE,         Buttons.KB_0,   Buttons.KB_ENTER,     Buttons.KB_SPEED_RES_DOWN,   # Scan 14
    ]

    # Third connection strip for LED = J19 on the LED board follows the following mapping. TODO Won't work with current automation board as of 4/22/24

    JUNKNOWN = [ # Data 6                16                        17                    18                       19                      20
        Buttons.K_LEFT_DISPLAY_SELECT,  None,                      None,                None,                    None,                   Buttons.K_TIME_MODE,            # Scan 11
        Buttons.K_MANUAL,               Buttons.K_CONSTANT_WATTS,  None,                None,                    None,                   None,                           # Scan 12
        None,                           Buttons.K_MINUS,           Buttons.K_TARGET_HR, None,                    None,                   None,                           # Scan 13
        None,                           None,                      Buttons.K_CHECKMARK, Buttons.K_ROLLING_HILLS, None,                   None,                           # Scan 14
        None,                           None,                      None,                Buttons.K_PLUS,          Buttons.K_FAT_BURN,     None,                           # Scan 15
        None,                           None,                      None,                None,                    Buttons.K_FITNESS_TEST, Buttons.K_RIGHT_DISPLAY_SELECT,  # Scan 16
    ]

class LEDConnectionsTM(Connections):
    """The map of items to connection points to pass to the Driver when it is setup. This supports All LED frame types. It does not support LED Group Training.
        LED Treadmill mapping is slightly different.
    """
    J200 = [ # Data 11                        12             13                    14                15
        Buttons.TV_LAST, 	          Buttons.TV_MUTE,     Buttons.TV_3, 	     Buttons.TV_2, 	    Buttons.TV_1,	     # Scan 15
        Buttons.TV_POWER,             None,		           Buttons.TV_6, 	     Buttons.TV_5, 	    Buttons.TV_4,	     # Scan 16
        Buttons.TV_CHANUP, 	          Buttons.TV_VOLUP,    Buttons.TV_9, 	     Buttons.TV_8, 	    Buttons.TV_7,	     # Scan 17
        Buttons.TV_CHANDOWN, 	      Buttons.TV_VOLDOWN,  Buttons.TV_ENTER,     Buttons.TV_0, 	    Buttons.TV_DASH,     # Scan 18
        Buttons.K_Q_INCLINE_RES_DOWN, None,                None,                 None,              None,                # Green
        Buttons.K_Q_SPEED_RES_DOWN,   Buttons.K_Q_STOP,    Buttons.K_Q_GO,       None,              None,                # RED
    ]                               # Treadmill USES D12,RED -> Buttons.K_Q_STOP and D13,RED -> Buttons.K_Q_GO

    J201 = LEDConnections.J201
