
import os, os.path
import glob
from PIL import Image
from Poster import Poster

def main():
    print('Lets start')
    x = 1
    imgarr = []
    path = 'F:\Dev\Python\HaloGrabber\screenshots'
    for filename in os.listdir(path):
        
        
        screenshot = Image.open(path + '\\' + filename)
        imgarr.append(screenshot)
    
    for f in imgarr:
        print("Posting Screenshot #" + str(x))
        Poster(f)
        x += 1
       

if __name__ == "__main__":
    main()