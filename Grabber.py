import numpy as np 
import os
from pynput import keyboard
from Snapper import Snapper


COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='9')},
    {keyboard.Key.shift, keyboard.KeyCode(char='(')}
]

current = set()

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            Snapper()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


def main():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
