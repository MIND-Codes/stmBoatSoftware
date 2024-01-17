# Author -  Luis Gerloni | MINDCode
# Email:    gerloni-luis@outlook.com

from paramiko import *
import os

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

client = SSHClient()
client.load_host_keys(r'C:\Users\luisg\.ssh\known_hosts')
client.load_system_host_keys()
client.set_missing_host_key_policy(AutoAddPolicy())

client.connect('192.168.169.61', username='mint', password='mintstm')
ftp = client.open_sftp()

cwd = os.getcwd()

def saveValue(fileName):
    try:
        ftp.put(fr'{cwd}\Values {fileName}.csv',
                fr'/home/mint/values/Values {fileName}.csv')

        os.remove(fr'{cwd}\Values {fileName}.csv')
    except Exception as error:
        print(f"{bcolors.FAIL}Error occurred: ", type(error).__name__)
        print(f"{bcolors.WARNING}Check if date is entered like this: 'Year-Month-Day.Hour-Minute'")