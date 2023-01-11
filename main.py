import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision
import MiningBot
import MiningBot_Utilities
import pyautogui as pt
from time import sleep
import torch
from PIL import ImageGrab





close_to_tree_threshold = 250000
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
model = torch.hub.load('.', 'custom', path="best.pt", source='local')
model.conf = 0.5  # NMS confidence threshold
model.max_det = 10  # maximum number of detections per image
def countdownTimer():
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 5):
        print(".", end="", flush=True)
        sleep(1)
    print("Go")

countdownTimer()
tree_bot = MiningBot.MiningBot()
loop_time = time()

while(True):



    im = ImageGrab.grab()  # take a screenshot
    results = model(im)
    


    targets = results.pandas().xywh[0]
    targets = targets.loc[targets.name == 'oak']
    if len(targets)!=0:
        target = targets.sort_values('width').values[-1]
        x, y, w, h, c, l, n = target
        t = round(4*((x+w//2-980)/960),2)
        if abs(t)<0.1:
            tree_bot._moveCharacter('w',0.2)
        elif t>0:
            tree_bot._moveCharacter('num6', t)
        elif t<0:
            tree_bot._moveCharacter('num4', -t)
        if w*h>close_to_tree_threshold:
            tree_bot._moveCharacter('num4', 0.2)
            tree_bot._chopTree()
    else:
        tree_bot._moveCharacter('num6', 2)
    tree_bot._moveCharacter('w',0.2)



print('Done.')
