# Author    -   Luis Gerloni    |   MIND-Codes
# Author    -   Clara Steiner   |   MIND-Codes
# Email:    -   gerloni-luis@outlook.com
# Github:   -   https://github.com/MIND-Codes

# Imports
from paramiko import *
import os

# FTP-Client Setup
client = SSHClient()
client.load_host_keys(r'C:\Users\luisg\.ssh\known_hosts')
client.load_system_host_keys()
client.set_missing_host_key_policy(AutoAddPolicy())

# Connecting to FTP-Server
client.connect('192.168.169.61', username='mint', password='mintstm')
ftp = client.open_sftp()

# Get current working directory
cwd = os.getcwd()

# Function to download the files with data
def getValue(fileName):
    try:
        ftp.get(fr'/home/mint/values/Values {fileName}.csv',
                fr'{cwd}\Values {fileName}.csv')

    except Exception as error:
        print(f"Error occurred: ", type(error).__name__)
        print(f"Check if date is entered like this: 'Year-Month-Day.Hour-Minute'")