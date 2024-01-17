# Author    -   Luis Gerloni    |   MIND-Codes
# Author    -   Clara Steiner   |   MIND-Codes
# Email:    -   gerloni-luis@outlook.com
# Github:   -   https://github.com/MIND-Codes

#Importierungen
import OutputManager as out
import sys
import subprocess

# Checking if all required libraries are installed, if not, they get installed
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

# Output of the five most recent file names
print("These are the five most recent files:")
out.output_list()

active = True
while active:
    # Output of available commands
    print(f"List five more files    -> '0'")
    print(f"Evaluate file           -> '[Date]'")

    # Input
    actionInput = input(f'Enter action from above: ')
    actionInput.lower()

    # '0' -> next five file names, other inputs are read as a date and if existing get downloaded
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
