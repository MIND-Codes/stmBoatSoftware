import OutputManagerSoftware
import sys
import subprocess

required = {'csv', 'numpy', 'paramiko'}
for module in required:
    try:
        if module in sys.modules:
            print(f"Library {module} already installed")
        else:
            subprocess.check_call(['pip', 'install', module])
            print(f"Library {module} has been installed successfully")
    except Exception as error:
        print(f"Error with library {module}")
        print(error)

active = True
while active:
    print(f"")
    print(f"")

    actionInput = input(f'Enter action from above: ')
    actionInput.lower()

    if actionInput == '0' or actionInput == 'connect':
        SensorSoftware.connect()
    elif actionInput == '1' or actionInput == 'measure':
        SensorSoftware.measure()
    elif actionInput == '2' or actionInput == 'upload':
        SensorSoftware.upload()
    #elif actionInput == '3' or actionInput == 'pump':
    #if round < 4:
    #    PumpActivationSoftware.pump(round)
    #    print(f"Activated pump {round}!")
    #    round += 1
    #    print(f"Next input '3' will activate pump {round}")
    #else:
    #    print("All pumps have already been used!")
    elif actionInput == '4' or actionInput == 'exit':
        SensorSoftware.exit()
        sys.exit()
        print(f"{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}No valid Input. Please try again")

