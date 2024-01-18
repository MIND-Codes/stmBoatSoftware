# Author    -   Luis Gerloni    |   MIND-Codes
# Author    -   Clara Steiner   |   MIND-Codes
# Email:    -   gerloni-luis@outlook.com
# Github:   -   https://github.com/MIND-Codes

import sys
import Sensors

class c:
    INCIDENTAL = '\33[90m'
    ERROR = '\33[31m'
    SUCCESS = '\33[32m'
    WARNING = '\33[33m'
    HIGHLIGHT = '\33[34m'
    ENDC = '\033[0m'

print(f"{c.INCIDENTAL}STMBoatProh succesfully loaded")
active = True
round = 0
while active:
    print(f"{c.HIGHLIGHT}Connect devices -> '0' || 'connect'")
    print(f"{c.HIGHLIGHT}Measure data    -> '1' || 'measure'")
    print(f"{c.HIGHLIGHT}Upload file     -> '2' || 'upload'")
    print(f"{c.HIGHLIGHT}Activate pumps  -> '3' || 'pump'")
    print(f"{c.HIGHLIGHT}Exit code       -> '4' || 'exit'")

    actionInput = input(f'{c.ENDC}Enter action from above: ')
    actionInput.lower()

    if actionInput == '0' or actionInput == 'connect':
        Sensors.connect()
    elif actionInput == '1' or actionInput == 'measure':
        Sensors.measure()
    elif actionInput == '2' or actionInput == 'upload':
        Sensors.upload()
    elif actionInput == '3' or actionInput == 'pump':
        if round < 4:
            PumpActivationSoftware.pump(round)
            print(f"{c.SUCCESS}Activated pump {round}!")
            round += 1
            print(f"{c.INCIDENTAL}Next input '3' will activate pump {round}")
        else:
            print(f"{c.ERROR}All pumps have already been used!")
    elif actionInput == '4' or actionInput == 'exit':
        Sensors.exit()
        sys.exit()
        print(f"{c.ENDC}")
    else:
        print(f"{c.ERROR}No valid Input. Please try again")