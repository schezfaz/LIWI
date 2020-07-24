import os, yaml, pyautogui,threading, time

with open(r'vars.yaml') as file:
    variables = yaml.load(file, Loader=yaml.FullLoader)
print(variables)
local_device = "adbDevice"

def start_emulation():
    os.chdir(variables['local_scrcpy_path'])
    print("PWD: ", os.getcwd())

    start_scrcpy_cmd = "scrcpy --window-title " + local_device
    os.system(start_scrcpy_cmd)

def get_device():
    print("1")
    width, height = pyautogui.size()  # get screen resolution
    print(width, height)
    # app = application.Application()
    # app.adbDevice.SetFocus()
    # device_location = pyautogui.locateOnScreen(local_device)
    # print(device_location)

threading.Thread(target=start_emulation).start()
threading.Thread(target=get_device).start()


