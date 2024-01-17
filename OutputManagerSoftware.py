from transformation_curves import main
import csv
from paramiko import *

client = SSHClient()
client.load_host_keys(r'C:\Users\luisg\.ssh\known_hosts')
client.load_system_host_keys()
client.set_missing_host_key_policy(AutoAddPolicy())

client.connect('192.168.169.61', username='mint', password='mintstm')
ftp = client.open_sftp()
ftp.chdir('values')

l = []
for n in ftp.listdir():
    lstatout = str(ftp.lstat(n)).split()[0]
    if 'd' not in lstatout: l.append(n)
l.sort(reverse=True)

i = 0

def process(fileName):
    a_values = [[], [], [], [], [], []]
    fileName = f"Values {fileName}.csv"
    with open(fileName, "r") as csvfile:
        csv_file_reader = csv.reader(csvfile, delimiter=",")
        for i, row in enumerate(csv_file_reader):
            if i >= 1:
                a_values[0].append(row[0].split(":")[1])
                a_values[1].append(row[1])
                a_values[2].append(row[2])
                a_values[3].append(row[3])
                a_values[4].append(row[4])
                a_values[5].append(row[5])

    values = []
    for i in a_values:
        a = 0
        for value in i:
            a += float(value)
        values.append(a / len(i))

    print(values)

    list = ["Temperatur", "Sauerstoff", "pH", "Nitrat", "Ammonium", "Leitfähigkeit", "Phosphat", "BSB5"]

    print("--------------------Gewässergüteklasse--------------------")

    p = input("Phosphat: ")
    b = input("BSB5: ")

    if len(p) != 0 and len(b) != 0:

        values.append(float(p))
        values.append(float(b))
        index, ci, quality_class = main(values)

        for i in range(8):
            print(list[i] + ": ")
            print(str(index[i]), "⬛" * (int(index[i]) // 10) + "⬜" * (10 - (int(index[i]) // 10)))

        print("Gewässergüteklasse: " + str(ci))
        print(quality_class)


def output_list():
    global i
    for n in l[(5 * i):(5 * (i + 1))]:
        out = n.replace("Values ", "")
        out = out.replace(".csv", "")
        print(out)
    i += 1
