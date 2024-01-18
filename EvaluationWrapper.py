# Author    -   Luis Gerloni    |   MIND-Codes
# Author    -   Clara Steiner   |   MIND-Codes
# Email:    -   gerloni-luis@outlook.com
# Github:   -   https://github.com/MIND-Codes

import OutputManager as out
import sys
import subprocess

class c:
    INCIDENTAL = '\33[90m'
    ERROR = '\33[31m'
    SUCCESS = '\33[32m'
    WARNING = '\33[33m'
    HIGHLIGHT = '\33[34m'
    ENDC = '\033[0m'

required = {'csv', 'numpy', 'paramiko'}
for module in required:
    try:
        if module in sys.modules:
            print(f"{c.INCIDENTAL}Library {module} already installed")
        else:
            subprocess.check_call(['pip', 'install', module])
            print(f"{c.INCIDENTAL}Library {module} has been installed successfully")
    except Exception as error:
        print(f"{c.ERROR}Error with library {module}")
        print(error)

print(f"{c.HIGHLIGHT}These are the five most recent files:")
out.output_list()

active = True
while active:
    print(f"{c.WARNING}List five more files    -> '0'")
    print(f"{c.WARNING}Evaluate file           -> '[Date]'")

    actionInput = input(f'{c.ENDC}Enter action from above: ')
    actionInput.lower()

    if actionInput == '0':
        out.output_list()
    else:
        try:
            out.process(actionInput)
            exit()
        except Exception as error:
            print(f"{c.ERROR}Error occured while trying to finde file!")
            print(f"{c.WARNING}Check if input was correct")
            print(f"Error: {error}")
