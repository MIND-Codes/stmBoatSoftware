import OutputManager as out
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

print("These are the five most recent files:")
out.output_list()

active = True
while active:
    print(f"List five more files    -> '0'")
    print(f"Evaluate file           -> '[Date]'")

    actionInput = input(f'Enter action from above: ')
    actionInput.lower()

    if actionInput == '0':
        out.output_list()
    else:
        try:
            out.process(actionInput)
            exit()
        except Exception as error:
            print(f"Error occured while trying to finde file!")
            print(f"Check if input was correct")
            print(f"Error: {error}")
