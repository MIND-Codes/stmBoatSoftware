# Author -  Luis Gerloni | MINDCode
# Email:    gerloni-luis@outlook.com

from paramiko import *

client = SSHClient()
client.load_host_keys(r'C:\Users\luisg\.ssh\known_hosts')
client.load_system_host_keys()
client.set_missing_host_key_policy(AutoAddPolicy())

client.connect('192.168.169.61', username='mint', password='mintstm')
ftp = client.open_sftp()

def saveValue(fileName):
    try:
        ftp.put(fr'C:\Users\luisg\PycharmProjects\WasseranalysePascoPython\BoatProj\Values {fileName}.csv',
                fr'/home/mint/values/Values {fileName}.csv')
    except:
        print("Invalid date. Enter date like this: 'Year-Month-Day.Hour-Minute'")