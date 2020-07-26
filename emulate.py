import os, sys

local_scrcpy_path = sys.argv[1]
local_device = "adbDevice"

def start_emulation():
    os.chdir(local_scrcpy_path)
    print("PWD: ", os.getcwd())
    start_scrcpy_cmd = "scrcpy --window-x 500 --window-title " + local_device
    print(start_scrcpy_cmd)
    os.system(start_scrcpy_cmd)

start_emulation()


