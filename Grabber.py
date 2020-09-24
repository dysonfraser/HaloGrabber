import numpy as np 
import cv2
import pyautogui
from pynput import keyboard
from PIL import Image
import pytesseract
import os 

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'  # your path may be different


COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(vk=112)} 
]


def execute():
    print("-------Taking Screenshot-------")
    image = pyautogui.screenshot()

    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) [1]

    filename ="{}.png".format(os.getpid())
    filename2 ="{}.png".format(os.getpid())

    cv2.imwrite(filename, gray)
    cv2.imwrite(filename2, image)

    text = pytesseract.image_to_string(Image.open(filename))
    #os.remove(filename)
    print(text)

    f = open("data.txt","w+")
    
    print("Adding to file")
    f.write(text)
    print("Added")
    f.close

    cv2.imshow("Image", image)
    cv2.imshow("Output", gray)




pressed_vks = set()

def get_vk(key):
    return key.vk if hasattr(key, 'vk') else key.value.vk


def is_combination_pressed(combination):
    return all([get_vk(key) in pressed_vks for key in combination])


def on_press(key):
    vk = get_vk(key)
    pressed_vks.add(vk)

    for combination in COMBINATIONS:
        if is_combination_pressed(combination):
            execute()
            break
    

def on_release(key):
    vk = get_vk(key)
    pressed_vks.remove(vk)
    


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
# image = pyautogui.screenshot()

# image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

# cv2.imwrite("image1.png", image)