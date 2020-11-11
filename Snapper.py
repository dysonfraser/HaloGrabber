from PIL import Image
import cv2
from datetime import datetime
import pyautogui
import os


def Snapper():

    today = datetime.now()

    print("-------Taking Screenshot-------")
    screenshot = pyautogui.screenshot().convert("RGB")
    filename = today.strftime("%B%d,%Y,%H,%M,%S") + ".png"
    path = 'F:\Dev\Python\HaloGrabber\screenshots\\' + filename
    screenshot.save(path)
    
