# Author    -   Luis Gerloni    |   MIND-Codes
# Author    -   Clara Steiner   |   MIND-Codes
# Email:    -   gerloni-luis@outlook.com
# Github:   -   https://github.com/MIND-Codes

# Imports
import sys
import Sensors
import PumpActivation

# Class with color prefixes
class c:
    Incidental = '\33[90m'
    Error = '\33[31m'
    Warning = '33[33m'
    Highlight = '\33[34m'
    Stop = '\33[0m'

# Setup
print(f"{c.Incidental}STMBoatProh succesfully loaded")
active = True
round = 0
PumpActivation.pump_setup()

# Output with all commands available
while active:
    print(f"{c.Highlight}Connect devices -> '0' || 'connect'")
    print(f"{c.Highlight}Measure data    -> '1' || 'measure'")
    print(f"{c.Highlight}Upload file     -> '2' || 'upload'")
    print(f"{c.Highlight}Activate pumps  -> '3' || 'pump'")
    print(f"{c.Highlight}Exit code       H-> '4' || 'exit'")

    actionInput = input(f'{c.Stop}Enter action from above: ')
    actionInput.lower()

    # Commands
    if actionInput == '0' or actionInput == 'connect':
        Sensors.connect()
    elif actionInput == '1' or actionInput == 'measure':
        Sensors.measure()
    elif actionInput == '2' or actionInput == 'upload':
        Sensors.upload()
    elif actionInput == '3' or actionInput == 'pump':
        if round < 4:
            PumpActivationSoftware.pump(round)
            print(f"{c.Warning}Activated pump {round}!")
            round += 1
            print(f"{c.Warning}Next input '3' will activate pump {round}")
        else:
            print(f"{c.Warning}All pumps have already been used!")
    elif actionInput == '4' or actionInput == 'exit':
        Sensors.exit()
        sys.exit()
        print(f"{c.Stop}")
    else:
        print(f"{c.Error}No valid Input. Please try again")