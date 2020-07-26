import time
from subprocess import *
import yaml

with open(r'vars.yaml') as file:
    variables = yaml.load(file, Loader=yaml.FullLoader)
print(variables)

#Booting the Emulator
boot_emulator_cmd = 'python emulate.py ' + variables['local_scrcpy_path']
Popen(boot_emulator_cmd,creationflags=CREATE_NEW_CONSOLE)

#Entering PIN and Copying passcode
token = variables['token']
get_passcode_cmd = 'python get_passcode.py ' + str(token)
passcode = check_output(get_passcode_cmd)
print(str(passcode))