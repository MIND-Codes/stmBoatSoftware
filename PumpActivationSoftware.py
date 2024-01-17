import RPi.GPIO as GPIO
from time import sleep

def pump_setup():
	try:
		GPIO.setwarnings(False)
		pins = [3,5,7,8]
		GPIO.setmode(GPIO.BOARD)
		for pin in pins:
			GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)
		print("Pumps successfully set up!")
	except Exception as error:
		print("Error occurred, while trying to setup pumps: ", type(error).__name__)

def pump(round):
	pins = [3,5,7,8]
	GPIO.output(pins[round], GPIO.LOW)
	sleep(30)
	GPIO.output(pins[round], GPIO.HIGH)

