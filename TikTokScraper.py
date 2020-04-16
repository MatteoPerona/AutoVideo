import pyautogui
import webbrowser  
import os
from time import sleep
from time import time
from random import uniform
from random import randint
'''
Author: Matteo Perona
This software is made to scrape TikToks
It uses extremely inefficient methods to get around TikTok's scraper prevention
'''

def down():
    pyautogui.press('down')
    
def up():
    pyautogui.press('up')

def openH():
    pyautogui.press('right')
    
def closeH():
    pyautogui.press('left')

def copy():
    pyautogui.hotkey('command', 'c')

def paste():
    pyautogui.hotkey('command', 'v')
    
def newTab():
    pyautogui.hotkey('command', 't')
    
def closeTabs(num):
    for x in range(num):
        pyautogui.hotkey('command', 'w')

def save():
    pyautogui.hotkey('command', 's')
    
def inspect():
    pyautogui.hotkey('shift', 'command', 'c')

def altInspect():
    pyautogui.click(453, 527, button='right')
    for x in range (7):
        pyautogui.press('down')
    pyautogui.press('enter')

def altInspect2():
    for x in range (7):
        pyautogui.press('down')
    pyautogui.press('enter')
    
def enter():
    pyautogui.press('enter')
    
def tab():
    pyautogui.press('tab')
    
def escape():
    pyautogui.press('esc')
    
    

def findVid(vidNum, start, end):
    for x in range(8):
        down()
        sleep(uniform(start, end))
    for x in range(3):  
        openH()
        down()
    for x in range(2):
        down()
        openH()
    for x in range(vidNum):
        sleep(uniform(start, end))
        down()
        
        
def getVidHref(start, end):
    for x in range(4):
        openH()
        down()
        sleep(uniform(start, end))
    tab()
    enter()
    

def getVidSrc(start, end):
    for x in range(14):#<-------------------------THIS NUM IS A BIG ISSUE
        sleep(uniform(start, end))
        down()
    enter()
    copy()
    
    
def downloadVid(fileName, num):
    newTab()
    sleep(1)
    paste()
    enter()
    sleep(2)
    save()
    sleep(1)
    pyautogui.typewrite(fileName + str(num) + '.mp4')
    enter()
    sleep(1)
    escape()
    sleep(1)
    escape()
    sleep(2)
    closeTabs(3)
    

def trendingScrape(x, y, fileName, num):
    webbrowser.open('https://www.tiktok.com/trending?lang=en', new=0, autoraise = True)
    sleep(5)
    pyautogui.click(x-1200,y+600, button='right')#<-------------------------------
    altInspect2()
    sleep(3)
    pyautogui.click(x, y)#<--------------------------------
    sleep(1)
    findVid(randint(1, 3), .01, .04)
    getVidHref(0, .2)
    sleep(3)
    pyautogui.click(x-1200,y+600)#<-------------------------------
    altInspect()
    sleep(1)
    pyautogui.click(x, y)#<-------------------------------
    getVidSrc(0, .2)
    downloadVid(fileName, num)

    
def findTagVid(num):
    for x in range(7):
        down()
    for x in range(3):
        openH()
        down()
    for x in range(2):
        down()
        openH()
    for x in range(num):
        down()
    

def tagScrape(tag, x, y, fileName, num, profNum):
    webbrowser.open(f'https://www.tiktok.com/tag/{tag}?lang=en', new=0, autoraise = True)
    sleep(5)
    pyautogui.click(x-1200,y+600, button='right')#<-------------------------------
    altInspect2()
    sleep(3)
    pyautogui.click(x, y)#<--------------------------------
    sleep(1)
    findTagVid(profNum)
    getVidHref(0, .2)
    sleep(3)
    pyautogui.click(x-1200,y+600)#<-------------------------------
    altInspect()
    sleep(1)
    pyautogui.click(x, y)#<-------------------------------
    getVidSrc(0, .2)
    downloadVid(fileName, num)
    

def musicScrape(song, x, y, fileName, num, profNum):
    webbrowser.open(f'https://www.tiktok.com/music/{song}?lang=en', new=0, autoraise = True)
    sleep(5)
    pyautogui.click(x-1200,y+600, button='right')#<-------------------------------
    altInspect2()
    sleep(3)
    pyautogui.click(x, y)#<--------------------------------
    sleep(1)
    findTagVid(profNum)
    getVidHref(0, .2)
    sleep(3)
    pyautogui.click(x-1200,y+600)#<-------------------------------
    altInspect()
    sleep(1)
    pyautogui.click(x, y)#<-------------------------------
    getVidSrc(0, .2)
    downloadVid(fileName, num)
    

def profScrape(profile, x, y, fileName, num, profNum):
    webbrowser.open(f'https://www.tiktok.com/@{profile}?lang=en', new=0, autoraise = True)
    sleep(5)
    pyautogui.click(x-1200,y+600, button='right')#<-------------------------------
    altInspect2()
    sleep(3)
    pyautogui.click(x, y)#<--------------------------------
    sleep(1)
    findTagVid(profNum)
    getVidHref(0, .2)
    sleep(3)
    pyautogui.click(x-1200,y+600)#<-------------------------------
    altInspect()
    sleep(1)
    pyautogui.click(x, y)#<-------------------------------
    getVidSrc(0, .2)
    downloadVid(fileName, num)

    
def moveFiles(old_dir,new_dir,file_type):
    for r,d,f in os.walk(old_dir):
        for file in f:
            if file_type in file:
                os.rename(r+file, new_dir+file)