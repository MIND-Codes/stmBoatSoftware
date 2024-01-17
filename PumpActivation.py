# Author    -   Luis Gerloni    |   MIND-Codes
# Author    -   Clara Steiner   |   MIND-Codes
# Email:    -   gerloni-luis@outlook.com
# Github:   -   https://github.com/MIND-Codes

# Imports
import RPi.GPIO as GPIO
from time import sleep

class c:
    Incidental = '\33[90m'
    Error = '\33[31m'
    Warning = '33[33m'
    Highlight = '\33[34m'
    Stop = '\33[0m'

# Function to setup the pins of the Raspberry Pi
def pump_setup():
	try:
		GPIO.setwarnings(False)
		pins = [3,5,7,8]
		GPIO.setmode(GPIO.BOARD)
		for pin in pins:
			GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)
		print(f"{c.Incidental}Pumps successfully set up!")
	except Exception as error:
		print(f"{c.Error}Error occurred, while trying to setup pumps: ", type(error).__name__)

# Function to call the pumps one by one
def pump(round):
	pins = [3,5,7,8]
	GPIO.output(pins[round], GPIO.LOW)
	sleep(30)
	GPIO.output(pins[round], GPIO.HIGH)

