import sys

import SensorSoftware

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.OKCYAN}STMBoatProh succesfully loaded")
active = True
while active:
    print(f"{bcolors.OKBLUE}Connect devices -> '0' || 'connect'")
    print(f"{bcolors.OKBLUE}Measure data    -> '1' || 'measure'")
    print(f"{bcolors.OKBLUE}Upload file     -> '2' || 'upload'")
    print(f"{bcolors.OKBLUE}Exit code       -> '3' || 'exit'")

    actionInput = input(f'{bcolors.ENDC}Enter action from above: ')
    actionInput.lower()

    if actionInput == '0' or actionInput == 'connect':
        SensorSoftware.connect()
    elif actionInput == '1' or actionInput == 'measure':
        SensorSoftware.measure()
    elif actionInput == '2' or actionInput == 'upload':
        SensorSoftware.upload()
    elif actionInput == '3' or actionInput == 'exit':
        SensorSoftware.exit()
        sys.exit()
        print(f"{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}No valid Input. Please try again")