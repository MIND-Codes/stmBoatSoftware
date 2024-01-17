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

# Class for color prefixes
class c:
    Incidental = '\33[90m'
    Error = '\33[31m'
    Warning = '33[33m'
    Highlight = '\33[34m'
    Stop = '\33[0m'

#   s = sensors
#   v = values
s_O2, s_pH, s_nitrate, s_ammonium, s_conductivity = PASCOBLEDevice(), PASCOBLEDevice(), PASCOBLEDevice(), \
                                                    PASCOBLEDevice(), PASCOBLEDevice()
v_temp, v_O2, v_pH, v_nitrate, v_ammonium, v_conductivity = [], [], [], [], [], []
v_info = ["Uhrzeit", "Temperatur", "Sauerstoff", "pH-Wert", "Nitrat", "Phosphat", "Ammonium", "Leitfaehigkeit"]
time = []
germanTZ = pytz.timezone("Europe/Berlin")
germanTime = datetime.now(germanTZ)

# Datetime for file name: Year-Month-Day.Hour-Minute
date = germanTime.strftime(("%Y-%m-%d.%H-%M-%S")[:-3])

# Function to connect all sensors
def connect():
    try:
        s_O2.connect_by_id("402-771")
        s_pH.connect_by_id("246-232")
        s_nitrate.connect_by_id("698-399")
        s_ammonium.connect_by_id("557-561")
        s_conductivity.connect_by_id("600-282")

        print(f"{c.Incidental}All sensors connected successfully!")
    except Exception as error:
        print(f'{c.Error}Error occurred with some of the Sensors: ', type(error).__name__)
        proceed = input(f"{c.Error}Proceed with connected Sensors? Yes -> '1'  || No -> '0': ")
        proceed.lower()
        if proceed == 'yes' or proceed == '1':
            print(f'{c.Incidental}Proceeding...')
        else:
            s_O2.disconnect()
            s_pH.disconnect()
            s_nitrate.disconnect()
            s_ammonium.disconnect()
            s_conductivity.disconnect()

            sys.exit()

# Function to get the measurements and put them in a csv file
def measure():
    try:
        for n in range(10):
            v_temp.append(f'{s_conductivity.read_data("Temperature")}')
            v_O2.append(f'{s_O2.read_data("DO2Concentration")}')
            v_pH.append(f'{s_pH.read_data("pH")}')
            v_nitrate.append(f'{s_nitrate.read_data("ISENitrate")}')
            v_ammonium.append(f'{s_ammonium.read_data("ISEAmmonium")}{s_ammonium.get_measurement_unit("ISEAmmonium")}')
            v_conductivity.append(f'{s_conductivity.read_data("Conductivity")}')
            time.append(germanTime.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])
            sleep(0.5)

        with open(f'Values {date}.csv', 'w', newline='') as new_file:
            csv_writer = csv.writer(new_file)
            csv_writer.writerow(v_info)

            for n in range(10):
                # !!! FOLGENDES ANHÄNGEN, WENN ALLE SENSOREN VORHANDEN: '[time[n], v_temp[n], v_O2[n], v_pH[n], v_nitrate[n],
                #                                     v_ammonium[n], v_conductivity[n]]' !!!
                csv_writer.writerow([[time[n], v_temp[n], v_O2[n], v_pH[n], v_nitrate[n],
                                    v_ammonium[n], v_conductivity[n]]])
        print(f'{c.Highlight}File saved as "{date}"')

    except Exception as error:
        print(f'{c.Error}Error occured: ', type(error).__name__)
        print(f'{c.Error}Please check, if all sensors are connected correctly!')

# Function to upload a file
def upload():
    fileName = input(f'{c.Highlight}Enter date of file like this: "Year-Month-Day.Hour-Minute" ')
    saveValue(fileName)

# Function to exit the programm
def exit():
    s_O2.disconnect()
    s_pH.disconnect()
    s_nitrate.disconnect()
    s_ammonium.disconnect()
    s_conductivity.disconnect()



