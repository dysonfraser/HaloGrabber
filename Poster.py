from PIL import Image
import pytesseract
import gspread
import cv2
from datetime import datetime
import pyautogui
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request 
import os


pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'  # your path may be different


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("HaloGrabber-d529cdf29dba.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Grabber").sheet1

# data = sheet.get_all_records()


def Poster(screenshot):
    
    # preprocessing
    rgb_img = screenshot.crop((100, 180, 1790, 610))
    width, height = rgb_img.size

    x = 0
    fillins = []


    while x < width:
    
        y = 0
        while y < height:
            

            r, g, b = rgb_img.getpixel((x,y))
            rgb = (r + g + b) / 3
            if rgb < 90:
                rgb_img.putpixel((x,y), (255, 255 ,255))
            else:
                rgb_img.putpixel((x,y), (0,0,0))
                # fillins.append((x + 1,y))
                # fillins.append((x - 1, y))
                # fillins.append((x, y + 1))
                # fillins.append((x, y - 1))
                # fillins.append((x, y - 1))
                # fillins.append((x + 1,y + 1))
                # fillins.append((x - 1, y + 1))
                # fillins.append((x + 1, y - 1))
                # fillins.append((x - 1, y - 1))
        
                

            y += 1 
        x += 1

    for x in fillins:
        rgb_img.putpixel(x, (0,0,0))
   
    imgarr = []
    rewidth = 120
    reheight = 80
    namewidth = 1000
    nameheight = 50

    # TEAM ONE

    ## PLAYER ONE


    firstplayer = []
    firstplayername = rgb_img.crop((55,24,600,43)).resize((namewidth,nameheight))
    firstplayer.append(firstplayername)
    firstplayerscore = rgb_img.crop((930,8,993,39)).resize((rewidth,reheight))
    firstplayer.append(firstplayerscore)
    firstplayerkills = rgb_img.crop((1160,9,1218,39)).resize((rewidth,reheight))
    firstplayer.append(firstplayerkills)
    firstplayerassists = rgb_img.crop((1403,9,1444,39)).resize((rewidth,reheight))
    firstplayer.append(firstplayerassists)
    firstplayerdeaths = rgb_img.crop((1623,9,1674,39)).resize((rewidth,reheight))
    firstplayer.append(firstplayerdeaths)

    # firstplayername.show()
    # firstplayerscore.show()
    # firstplayerkills.show()
    # firstplayerassists.show()
    # firstplayerdeaths.show()

    imgarr.append(firstplayer)

    ## PLAYER TWO

    secondplayer = []
    secondplayername = rgb_img.crop((55,73,600,92)).resize((namewidth,nameheight))
    secondplayer.append(secondplayername)
    secondplayerscore = rgb_img.crop((930,55,993,86)).resize((rewidth,reheight))
    secondplayer.append(secondplayerscore)
    secondplayerkills = rgb_img.crop((1160,55,1218,86)).resize((rewidth,reheight))
    secondplayer.append(secondplayerkills)
    secondplayerassists = rgb_img.crop((1403,55,1444,86)).resize((rewidth,reheight))
    secondplayer.append(secondplayerassists)
    secondplayerdeaths = rgb_img.crop((1623,55,1674,86)).resize((rewidth,reheight))
    secondplayer.append(secondplayerdeaths)

    # secondplayername.show()
    # secondplayerscore.show()
    # secondplayerkills.show()
    # secondplayerassists.show()
    # secondplayerdeaths.show()

    imgarr.append(secondplayer)


    ## PLAYER THREE

    thirdplayer = []
    thirdplayername = rgb_img.crop((55,122,600,140)).resize((namewidth,nameheight))
    thirdplayer.append(thirdplayername)
    thirdplayerscore = rgb_img.crop((930,105,993,140)).resize((rewidth,reheight))
    thirdplayer.append(thirdplayerscore)
    thirdplayerkills = rgb_img.crop((1160,105,1218,140)).resize((rewidth,reheight))
    thirdplayer.append(thirdplayerkills)
    thirdplayerassists = rgb_img.crop((1403,105,1444,140)).resize((rewidth,reheight))
    thirdplayer.append(thirdplayerassists)
    thirdplayerdeaths = rgb_img.crop((1623,105,1674,140)).resize((rewidth,reheight))
    thirdplayer.append(thirdplayerdeaths)

    # thirdplayername.show()
    # thirdplayerscore.show()
    # thirdplayerkills.show()
    # thirdplayerassists.show()
    # thirdplayerdeaths.show()


    imgarr.append(thirdplayer)

    ## PLAYER FOUR

    fourthplayer = []
    fourthplayername = rgb_img.crop((55,170,600,192)).resize((namewidth,nameheight))
    fourthplayer.append(fourthplayername)
    fourthplayerscore = rgb_img.crop((930,155,993,192)).resize((rewidth,reheight))
    fourthplayer.append(fourthplayerscore)
    fourthplayerkills = rgb_img.crop((1160,155,1218,192)).resize((rewidth,reheight))
    fourthplayer.append(fourthplayerkills)
    fourthplayerassists = rgb_img.crop((1403,155,1444,192)).resize((rewidth,reheight))
    fourthplayer.append(fourthplayerassists)
    fourthplayerdeaths = rgb_img.crop((1623,155,1674,192)).resize((rewidth,reheight))
    fourthplayer.append(fourthplayerdeaths)


    # fourthplayername.show()
    # fourthplayerscore.show()
    # fourthplayerkills.show()
    # fourthplayerassists.show()
    # fourthplayerdeaths.show()

    imgarr.append(fourthplayer)

    # TEAM TWO

    ## PLAYER FIVE
    fifthplayer = []
    fifthplayername = rgb_img.crop((55,221,689,239)).resize((namewidth,nameheight))
    fifthplayer.append(fifthplayername)
    fifthplayerscore = rgb_img.crop((930,205,993,239)).resize((rewidth,reheight))
    fifthplayer.append(fifthplayerscore)
    fifthplayerkills = rgb_img.crop((1160,205,1218,239)).resize((rewidth,reheight))
    fifthplayer.append(fifthplayerkills)
    fifthplayerassists = rgb_img.crop((1403,205,1444,239)).resize((rewidth,reheight))
    fifthplayer.append(fifthplayerassists)
    fifthplayerdeaths = rgb_img.crop((1623,205,1674,239)).resize((rewidth,reheight))
    fifthplayer.append(fifthplayerdeaths)



    imgarr.append(fifthplayer)


    ## PLAYER SIX
    sixthplayer =[]
    sixthplayername = rgb_img.crop((55,270,600,290)).resize((namewidth,nameheight))
    sixthplayer.append(sixthplayername)
    sixthplayerscore = rgb_img.crop((930,255,993,290)).resize((rewidth,reheight))
    sixthplayer.append(sixthplayerscore)
    sixthplayerkills = rgb_img.crop((1160,255,1218,290)).resize((rewidth,reheight))
    sixthplayer.append(sixthplayerkills)
    sixthplayerassists = rgb_img.crop((1403,255,1444,290)).resize((rewidth,reheight))
    sixthplayer.append(sixthplayerassists)
    sixthplayerdeaths = rgb_img.crop((1623,255,1674,290)).resize((rewidth,reheight))
    sixthplayer.append(sixthplayerdeaths)


    imgarr.append(sixthplayer)


    ## PLAYER SEVEN
    seventhplayer = []
    seventhplayername = rgb_img.crop((55,320,689,340)).resize((namewidth,nameheight))
    seventhplayer.append(seventhplayername)
    seventhplayerscore = rgb_img.crop((930,305,993,340)).resize((rewidth,reheight))
    seventhplayer.append(seventhplayerscore)
    seventhplayerkills = rgb_img.crop((1160,305,1218,340)).resize((rewidth,reheight))
    seventhplayer.append(seventhplayerkills)
    seventhplayerassists = rgb_img.crop((1403,305,1444,340)).resize((rewidth,reheight))
    seventhplayer.append(seventhplayerassists)
    seventhplayerdeaths = rgb_img.crop((1623,305,1674,340)).resize((rewidth,reheight))
    seventhplayer.append(seventhplayerdeaths)

    imgarr.append(seventhplayer)

    ## PLAYER EIGHT
    eighthplayer = []
    eighthplayername = rgb_img.crop((55,367,600,390)).resize((namewidth,nameheight))
    eighthplayer.append(eighthplayername)
    eighthplayerscore = rgb_img.crop((930,340,993,390)).resize((rewidth,reheight))
    eighthplayer.append(eighthplayerscore)
    eighthplayerkills = rgb_img.crop((1160,340,1218,390)).resize((rewidth,reheight))
    eighthplayer.append(eighthplayerkills)
    eighthplayerassists = rgb_img.crop((1403,340,1444,390)).resize((rewidth,reheight))
    eighthplayer.append(eighthplayerassists)
    eighthplayerdeaths = rgb_img.crop((1623,340,1674,390)).resize((rewidth,reheight))
    eighthplayer.append(eighthplayerdeaths)


    # eighthplayername.show()
    # eighthplayerscore.show()
    # eighthplayerkills.show()
    # eighthplayerassists.show()
    # eighthplayerdeaths.show()


    imgarr.append(eighthplayer)



    # rgb_img.show()
    # firstplayername.show()
    # secondplayername.show()
    # thirdplayername.show()
    # fourthplayername.show()
    # fifthplayername.show()
    # sixthplayername.show()
    # seventhplayername.show()
    # eightplayername.show()


    insert = []
    for y in imgarr:
        values = []
        i = 0
        for x in y:
            text = pytesseract.image_to_string(x, config="--psm 7")
            newword = ''
            if i > 0:
                
                for char in text:
                    if char == '\'':
                        tempword = newword + ''
                    elif char == 'b' or char == 'B':
                        tempword = newword + '8'
                    elif char == '|' or char == 'l':
                        tempword = newword + '1'
                    elif char == '/':
                        tempword = newword + '7'
                    elif char == 's' or char == 'S':
                        tempword = newword + '5'
                    elif char == ' ':
                        tempword = newword + ''
                    elif char == 'D':
                        tempword = newword + '0' 
                    elif char == '?':
                        tempword = newword + '2'
                    else:
                        tempword = newword + char
                    newword = tempword
            else:
                newword = text

            text = newword.rstrip('\n\x0c')
            
            #convert stats to ints while ignoring tesseract errors
            try:
                text = int(text)

            except ValueError as nint:
                pass
            
            
            values.append(text)
            print(text)
            i += 1
        
        insert.append(values)

    insert_row = int(sheet.cell(1,6).value)


    for x in insert:
        print(x)
        sheet.insert_row(x,insert_row)
        insert_row += 1


    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    sheet.insert_row([currentTime],insert_row)
    insert_row += 1
    sheet.update_cell(1,6,insert_row)
