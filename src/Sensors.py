# Author    -   Luis Gerloni    |   MIND-Codes
# Author    -   Clara Steiner   |   MIND-Codes
# Email:    -   gerloni-luis@outlook.com
# Github:   -   https://github.com/MIND-Codes

# Imports
import sys
from pasco import PASCOBLEDevice
from datetime import datetime
import csv
import pytz
from FTPUpload import saveValue
from time import sleep


# Class for colored outputs
class c:
    INCIDENTAL = '\33[90m'
    ERROR = '\33[31m'
    SUCCESS = '\33[32m'
    WARNING = '\33[33m'
    HIGHLIGHT = '\33[34m'
    ENDC = '\033[0m'


#   s = sensors
#   v = values
s_O2, s_pH, s_nitrate, s_ammonium, s_conductivity = PASCOBLEDevice(), PASCOBLEDevice(), PASCOBLEDevice(), \
                                                    PASCOBLEDevice(), PASCOBLEDevice()
v_temp, v_O2, v_pH, v_nitrate, v_ammonium, v_conductivity = [], [], [], [], [], []
v_info = ["Uhrzeit", "Temperatur", "Sauerstoff", "pH-Wert", "Nitrat", "Phosphat", "Ammonium", "Leitfaehigkeit"]
time = []
germanTZ = pytz.timezone("Europe/Berlin")
germanTime = datetime.now(germanTZ)

# Time format: Year-Month-Day.Hour-Minute-Second
date = germanTime.strftime(("%Y-%m-%d.%H-%M-%S")[:-3])


# Function to connect to all sensors
def connect():
    try:
        s_O2.connect_by_id("402-771")
        print(f"{c.INCIDENTAL}O2 connected")
        s_pH.connect_by_id("246-232")
        print(f"{c.INCIDENTAL}pH connected")
        s_nitrate.connect_by_id("698-399")
        print(f"{c.INCIDENTAL}Nitrate connected")
        s_ammonium.connect_by_id("557-561")
        print(f"{c.INCIDENTAL}Ammonium connected")
        s_conductivity.connect_by_id("600-282")
        print(f"{c.INCIDENTAL}Conductivity connected")

        print(f"{c.SUCCESS}All sensors connected successfully!")
    except Exception as error:
        print(f'{c.ERROR}Error occurred with some of the Sensors: ', type(error).__name__)
        proceed = input(f"{c.WARNING}Proceed with connected Sensors? Yes -> '1'  || No -> '0': ")
        proceed.lower()
        if proceed == 'yes' or proceed == '1':
            print(f'{c.INCIDENTAL}Proceeding...')
        else:
            s_O2.disconnect()
            s_pH.disconnect()
            s_nitrate.disconnect()
            s_ammonium.disconnect()
            s_conductivity.disconnect()

            sys.exit()


# Function to get measurements from the sensors
def measure():
    try:
        for n in range(10):
            print(f"{c.INCIDENTAL}Measurement round {n}")
            v_temp.append(f'{s_conductivity.read_data("Temperature")}')
            v_O2.append(f'{s_O2.read_data("DO2Concentration")}')
            v_pH.append(f'{s_pH.read_data("pH")}')
            v_nitrate.append(f'{s_nitrate.read_data("ISENitrate")}')
            v_ammonium.append(f'{s_ammonium.read_data("ISEAmmonium")}')
            v_conductivity.append(f'{s_conductivity.read_data("Conductivity")}')
            time.append(germanTime.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])
            sleep(0.5)

        with open(f'Values {date}.csv', 'w', newline='') as new_file:
            csv_writer = csv.writer(new_file)
            csv_writer.writerow(v_info)

            for n in range(10):
                # !!! FOLGENDES ANHÄNGEN, WENN ALLE SENSOREN VORHANDEN: '[time[n], v_temp[n], v_O2[n], v_pH[n], v_nitrate[n],
                #                                     v_ammonium[n], v_conductivity[n]]' !!!
                csv_writer.writerow([time[n], v_temp[n], v_O2[n], v_pH[n], v_nitrate[n],
                                     v_ammonium[n], v_conductivity[n]])
        print(f'{c.SUCCESS}File saved as "{date}"')

    except Exception as error:
        print(f'{c.ERROR}Error occured: ', type(error).__name__)
        print(f'{c.WARNING}Please check, if all sensors are connected correctly!')


# Function to call the upload in FTPUpload
def upload():
    fileName = input(f'{c.WARNING}Enter date of file like this: "Year-Month-Day.Hour-Minute" ')
    saveValue(fileName)


# Function to exit the programm
def exit():
    s_O2.disconnect()
    s_pH.disconnect()
    s_nitrate.disconnect()
    s_ammonium.disconnect()
    s_conductivity.disconnect()
