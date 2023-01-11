################
## Main Logic ##

import pyautogui as pt
from time import sleep
import pydirectinput as pdi


def main():
    initializePyAutoGUI()
    countdownTimer()
    clickResumeGame()
    chopTree()
    #reportMousePosition(seconds=5)
    return 0

def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    pt.FAILSAFE = True


def countdownTimer():
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 5):
        print(".", end="", flush=True)
        sleep(1)
    print("Go")



def holdKey(key, seconds=1.00):
    pt.keyDown(key)
    sleep(seconds)
    pt.keyUp(key)

def chopTree():
    holdKey('q', 3.3)
    holdKey('num2', 0.5)
    holdKey('q', 3.3)
    holdKey('w', 0.08)
    holdKey('num8', 2)
    holdKey('q', 3.3)
    holdKey('q', 3.3)
    holdKey('num2', 0.91)

def reportMousePosition(seconds=10):
    for i in range(0, seconds):
        print(pt.position())
        sleep(1)

def clickResumeGame():
    pdi.moveTo(420, 320)
    pdi.click()
    sleep(1)

if __name__ == "__main__":
    main()