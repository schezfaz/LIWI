import pyautogui
import time
import win32clipboard
from autogui import *

token = sys.argv[1]

#Waiting for scrcpy server to boot completely
time.sleep(4)
setWindow("adbDevice")


def passcode():
    pyautogui.moveTo(670, 730)
    pyautogui.click(x=670, y=730, clicks=2, button='left')
    time.sleep(2)
    # print("RSA: ", pyautogui.locateOnScreen('token.png'))
    pyautogui.typewrite(token)
    pyautogui.click(x=1000, y=400, clicks=2, button='left')
    time.sleep(2)
    pyautogui.click(x=727, y=889, clicks=2, button='left')

def get_clipboard_contents():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    print(data)

passcode()
time.sleep(4)
get_clipboard_contents()



