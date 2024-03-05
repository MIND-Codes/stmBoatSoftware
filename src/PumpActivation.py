# Author    -   Luis Gerloni    |   MIND-Codes
# Author    -   Clara Steiner   |   MIND-Codes
# Email:    -   gerloni-luis@outlook.com
# Github:   -   https://github.com/MIND-Codes

# Imports
import RPi.GPIO as GPIO
from time import sleep


# Class for colored outputs
class c:
    INCIDENTAL = '\33[90m'
    ERROR = '\33[31m'
    SUCCESS = '\33[32m'
    WARNING = '\33[33m'
    HIGHLIGHT = '\33[34m'
    ENDC = '\033[0m'


# Function to setup everything needed for the Raspberry Pis pins,
# which are responsible for the pumps
def pump_setup():
    try:
        GPIO.setwarnings(False)
        pins = [3, 5, 7, 8]
        GPIO.setmode(GPIO.BOARD)
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)
        print(f"{c.SUCCESS}Pumps successfully set up!")
    except Exception as error:
        print(f"{c.ERROR}Error occurred, while trying to setup pumps: ", type(error).__name__)


# Function to activate tue pumps one by one
def pump(round):
    pins = [3, 5, 7, 8]
    GPIO.output(pins[round], GPIO.LOW)
    sleep(30)
    GPIO.output(pins[round], GPIO.HIGH)
