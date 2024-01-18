# Author    -   Luis Gerloni    |   MIND-Codes
# Author    -   Clara Steiner   |   MIND-Codes
# Email:    -   gerloni-luis@outlook.com
# Github:   -   https://github.com/MIND-Codes

from paramiko import *
import os


class c:
    INCIDENTAL = '\33[90m'
    ERROR = '\33[31m'
    SUCCESS = '\33[32m'
    WARNING = '\33[33m'
    HIGHLIGHT = '\33[34m'
    ENDC = '\033[0m'


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
        print(f"{c.ERROR}Error occurred: ", type(error).__name__)
        print(f"{c.WARNING}Check if date is entered like this: 'Year-Month-Day.Hour-Minute'")
