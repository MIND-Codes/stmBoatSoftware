# Author -  Luis Gerloni | MINDCode
# Email:    gerloni-luis@outlook.com
import sys

from pasco import PASCOBLEDevice
from datetime import datetime
import csv
import pytz
from FTPUploadSoftware import saveValue
from time import sleep

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

#   s = sensors
#   v = values
s_O2, s_pH, s_nitrate, s_ammonium, s_conductivity = PASCOBLEDevice(), PASCOBLEDevice(), PASCOBLEDevice(), \
                                                    PASCOBLEDevice(), PASCOBLEDevice()
v_temp, v_O2, v_pH, v_nitrate, v_ammonium, v_conductivity = [], [], [], [], [], []
v_info = ["Uhrzeit", "Temperatur", "Sauerstoff", "pH-Wert", "Nitrat", "Phosphat", "Ammonium", "Leitfaehigkeit"]
time = []
germanTZ = pytz.timezone("Europe/Berlin")
germanTime = datetime.now(germanTZ)
# Zeit für die Dateibenennung: Jahr-Monat-Tag_Stunde-Minute-Sekunde
date = germanTime.strftime(("%Y-%m-%d.%H-%M-%S")[:-3])

def connect():
    try:
        print(1)
        #s_O2.connect_by_id("402-771")
        print(2)
        #s_pH.connect_by_id("246-232")
        print(3)
        s_nitrate.connect_by_id("551-660")
        print(4)
        s_ammonium.connect_by_id("698-399")
        print(5)
        #s_conductivity.connect_by_id("600-282")
        print(6)

        print(f"{bcolors.OKGREEN}All sensors connected successfully!")
    except Exception as error:
        print(f'{bcolors.FAIL}Error occurred with some of the Sensors: ', type(error).__name__)
        proceed = input("Proceed with connected Sensors? Yes -> '1'  || No -> '0': ")
        proceed.lower()
        if proceed == 'yes' or proceed == '1':
            print('Proceeding...')
        else:
            s_O2.disconnect()
            s_pH.disconnect()
            s_nitrate.disconnect()
            #s_ammonium.disconnect()
            s_conductivity.disconnect()

            sys.exit()

def measure():
    try:
        for n in range(10):
            print(1)
            v_temp.append(f'{s_conductivity.read_data("Temperature")}')
            print(2)
            v_O2.append(f'{s_O2.read_data("DO2Concentration")}')
            print(3)
            v_pH.append(f'{s_pH.read_data("pH")}')
            print(4)
            v_nitrate.append(f'{s_nitrate.read_data("ISENitrate")}')
            print(5)
            #v_ammonium.append(f'{s_ammonium.read_data("ISEAmmonium")}{s_ammonium.get_measurement_unit("ISEAmmonium")}')
            v_conductivity.append(f'{s_conductivity.read_data("Conductivity")}')
            print(6)
            time.append(germanTime.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])
            print(7)
            sleep(0.5)

        with open(f'Values {date}.csv', 'w', newline='') as new_file:
            csv_writer = csv.writer(new_file)
            csv_writer.writerow(v_info)

            for n in range(10):
                # !!! FOLGENDES ANHÄNGEN, WENN ALLE SENSOREN VORHANDEN: '[time[n], v_temp[n], v_O2[n], v_pH[n], v_nitrate[n],
                #                                     v_ammonium[n], v_conductivity[n]]' !!!
                csv_writer.writerow([time[n], v_temp[n], v_O2[n], v_pH[n], v_nitrate[n], v_conductivity[n]])
        print(f'{bcolors.OKGREEN}File saved as "{date}"')

    except Exception as error:
        print(f'{bcolors.FAIL}Error occured: ', type(error).__name__)
        print(f'{bcolors.WARNING}Please check, if all sensors are connected correctly!')

def upload():
    fileName = input(f'{bcolors.OKBLUE}Enter date of file like this: "Year-Month-Day.Hour-Minute" ')
    saveValue(fileName)

def exit():
    s_O2.disconnect()
    s_pH.disconnect()
    s_nitrate.disconnect()
    s_ammonium.disconnect()
    s_conductivity.disconnect()



