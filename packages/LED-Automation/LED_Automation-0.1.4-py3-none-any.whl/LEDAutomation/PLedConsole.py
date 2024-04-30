from Connections import Connections, Buttons

# Mappings sourced from:
# https://bitbucket.org/johnsonhealthtech/raven_io_gd32f305ve/src/master/Modules/Key_Lib/Keyboard.c 

class PLEDConnections(Connections):
    """The map of items to connection points to pass to the Driver when it is setup"""
    J200 = [ # Data 11                   12                      13                      14                      15
        Buttons.TV_LAST,                 Buttons.TV_MUTE,       Buttons.TV_3,         Buttons.TV_2,        Buttons.TV_1,    # Scan 15
        Buttons.TV_POWER,                None,                  Buttons.TV_6,         Buttons.TV_5,        Buttons.TV_4,    # Scan 16
        Buttons.TV_CHANUP,               Buttons.TV_VOLUP,      Buttons.TV_9,         Buttons.TV_8,        Buttons.TV_7,    # Scan 17
        Buttons.TV_CHANDOWN,             Buttons.TV_VOLDOWN,    Buttons.TV_ENTER,     Buttons.TV_0,        Buttons.TV_DASH, # Scan 18
        None,                            None,                  None,                 None,                None,            # Scan Green
        None,                            None,                  None,                 None,                None,            # Scan Red
    ]

    J201 = [ # Data 11                  12                      13              14                15
        Buttons.KB_INCLINE_RES_DOWN,    Buttons.KB_1,           Buttons.KB_2,   Buttons.KB_3,     Buttons.KB_SPEED_RES_UP,     # Scan 11
        Buttons.KB_INCLINE_RES_UP,      Buttons.KB_STOP,        Buttons.KB_4,   Buttons.KB_5,     Buttons.KB_6,                # Scan 12
        Buttons.KB_RUN,                 Buttons.KB_7,           Buttons.KB_8,   Buttons.KB_9,     Buttons.KB_CONCIERGE,        # Scan 13
        Buttons.KB_PAUSE,               Buttons.KB_DELETE,      Buttons.KB_0,   Buttons.KB_ENTER, Buttons.KB_SPEED_RES_DOWN,   # Scan 14
        None,                           None,                   None,           None,             None,                        # Scan Green
    ]

    J202 = [
        Buttons.ATM_RIGHT_1,    Buttons.ATM_RIGHT_2,    Buttons.ATM_RIGHT_3,    Buttons.ATM_RIGHT_4
    ]

    J203 = [
        Buttons.ATM_LEFT_1,     Buttons.ATM_LEFT_2,     Buttons.ATM_LEFT_3,     Buttons.ATM_LEFT_4
    ]
