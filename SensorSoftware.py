# Author -  Luis Gerloni | MINDCode
# Email:    gerloni-luis@outlook.com
import sys

from pasco import PASCOBLEDevice
from datetime import datetime
import csv
import pytz
from FTPUploadSoftware import saveValue

#   s = sensors
#   v = values
s_O2, s_pH, s_nitrate, s_ammonium, s_conductivity = PASCOBLEDevice(), PASCOBLEDevice(), PASCOBLEDevice(), \
                                                    PASCOBLEDevice(), PASCOBLEDevice()
v_temp, v_O2, v_pH, v_nitrate, v_ammonium, v_conductivity = [], [], [], [], [], []
v_info = ["Uhrzeit", "Temperatur", "Sauerstoff", "pH-Wert", "Nitrat", "Phosphat", "Ammoniak", "Leitfaehigkeit"]
time = []

try:
    #s_O2.connect_by_id("402-771")
    #s_pH.connect_by_id("246-232")
    #s_nitrate.connect_by_id("557-561")
    #s_ammonium.connect_by_id("551-660")
    s_conductivity.connect_by_id("926-046")
except Exception as error:
    print('Error occured: ', type(error).__name__)
    proceed = input('Proceed anyways? | Yes (1); No (0)')
    proceed.lower()
    if proceed == 'yes' or proceed == '1':
        print('Proceeding...')
    else:
        s_O2.disconnect()
        s_pH.disconnect()
        s_nitrate.disconnect()
        s_ammonium.disconnect()
        s_conductivity.disconnect()

        sys.exit()

germanTZ = pytz.timezone("Europe/Berlin")
germanTime = datetime.now(germanTZ)

active = True

# Zeit für die Dateibenennung: Jahr-Monat-Tag_Stunde-Minute-Sekunde
date = germanTime.strftime(("%Y-%m-%d.%H-%M-%S")[:-3])

while active:

    action = input("Enter action | measure (0); transfer (1); exit (3)")

    if action == 'measure' or action == '0':

        for n in range(10):
            v_temp.append(f'{s_conductivity.read_data("Temperature")}{s_conductivity.get_measurement_unit("Temperature")}')
            #v_O2.append(f'{s_O2.read_data("DO2Concentration")}{s_O2.get_measurment_unit("DO2Concentration")}')
            #v_pH.append(f'{s_pH.read_data("pH")}{s_pH.get_measurement_unit("pH")}')
            #v_nitrate.append(f'{s_nitrate.read_data("ISENitrate")}{s_nitrate.get_measurement_unit("ISENitrate")}')
            #v_ammonium.append(f'{s_ammonium.read_data("ISEAmmonium")}{s_ammonium.get_measurement_unit("ISEAmmonium")}')
            #v_conductivity.append(f'{s_conductivity.read_data("Conductivity")}{s_conductivity.get_measurement_unit("Conductivity")}')
            time.append(germanTime.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])

        with open(f'Values {date}.csv', 'w', newline='') as new_file:
            csv_writer = csv.writer(new_file)

            csv_writer.writerow(v_info)

            for n in range(10):
                # !!! FOLGENDES ANHÄNGEN, WENN ALLE SENSOREN VORHANDEN: ', v_O2[n], v_pH[n], v_nitrate[n],
                #                             v_ammonium[n], v_conductivity[n]' !!!
                csv_writer.writerow([time[n], v_temp[n]])

        print(f'File saved as "{date}"')

    elif action == 'transfer' or action == '1':
        fileName = input('Enter date of file like this: "Year-Month-Day.Hour-Minute"')
        saveValue(fileName)

    elif action == 'exit' or action == '2':

        s_O2.disconnect()
        s_pH.disconnect()
        s_nitrate.disconnect()
        s_ammonium.disconnect()
        s_conductivity.disconnect()

        active = False



