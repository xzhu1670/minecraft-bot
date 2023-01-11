import cv2 as cv
import numpy as np
import os
from time import time
from WindowCapture import WindowCapture
from vision import Vision
import MiningBot
import MiningBot_Utilities
import pyautogui as pt
from time import sleep
# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture()
# initialize the Vision class
vision_tree = Vision('images/tree6.jpg')

'''
# https://www.crazygames.com/game/guns-and-bottle
wincap = WindowCapture()
vision_gunsnbottle = Vision('gunsnbottle.jpg')
'''
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
countdownTimer()
tree_bot = MiningBot.MiningBot()
# loop_time = time()
while(True):
    
    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # display the processed image
    points = vision_tree.find(screenshot, 0.5)#'rectangles')
    #points = vision_gunsnbottle.find(screenshot, 0.7, 'points')
    if points:
        print(points)
        t = round(4*((points[0][0]-960)/960),2)
        if t>0:
            tree_bot._moveCharacter('num6', t)
            tree_bot._moveCharacter('w',1)
        elif t<0:
            tree_bot._moveCharacter('num4', -t)
            tree_bot._moveCharacter('w',1)
        else:
            tree_bot._moveCharacter('w',1)

    # debug the loop rate
    # print('FPS {}'.format(1 / (time() - loop_time)))
    # loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('p'):
        cv.destroyAllWindows()
        break

print('Done.')