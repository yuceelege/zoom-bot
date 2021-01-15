import pyautogui
import subprocess
import time
from datetime import datetime
import numpy as np
import webbrowser
import interface
import tkinter as tk
import os
import sys



def initiate_schedule():
    root = tk.Tk()
    page = interface.Window(root)
    root.mainloop()

def exec_time(day,time):
    days= ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    try:
        return (days.index(day.lower()),time)
    except:
        print('You have to type the day correctly. Start Again :(')
        os.remove('data.csv')
        sys.exit()


def exist(image):
    try:
        if len(pyautogui.locateCenterOnScreen(image)) == 2:
            return True
    except Exception:
        return False
    
def centralize():
    x = pyautogui.size()
    pyautogui.moveTo(x[0]//2, x[1]//2)
    time.sleep(0.1)
    pyautogui.moveTo(500, 500)


def image_click(file):
    iconX, iconY = pyautogui.locateCenterOnScreen(file)
    pyautogui.click(iconX, iconY)
    return iconX, iconY

def full_screen():
    time.sleep(2)
    if exist('images\full_screen.png'):
        iconX, iconY = pyautogui.locateCenterOnScreen('images\full_screen.png')
        pyautogui.click(iconX+170, iconY)
        

def sign_in(credential=False,link=False):
    if link == False:
        meeting_id = credential.split('@xox@')[0]
        pwd = credential.split('@xox@')[1]
        subprocess.call('start Zoom',shell=True)
        time.sleep(7)
        try:
            image_click('images\join.png')
        except:
            image_click('images\join2.png')
        time.sleep(3)
        pyautogui.write(meeting_id, interval=0.25)
        pyautogui.press('enter')
        wait = True
        while wait:
            if exist('images\passcode.png'):
                wait = False
        pyautogui.write(pwd, interval=0.25)
        pyautogui.press('enter')
        return True
    elif credential == False:
        webbrowser.open_new(link)
        time.sleep(7)
        waiting_room = True
        while waiting_room:
            if exist('images\full_screen.png'):
                if not exist('images\waiting_room'):
                    waiting_room = False
            time.sleep(0.5)
        for i in range(9):
            if exist('images\link_join.png'):
                time.sleep(1.5)
                image_click('images\link_join.png')
                break
            time.sleep(3)
    time.sleep(10)
    full_screen()
    for i in range(4):
        if exist('images\mic_on.png'):
            image_click('images\mic_on.png')
        time.sleep(0.8)
        centralize()
        time.sleep(0.8)
        if exist('images\cam_on.png'):
            image_click('images\cam_on.png')
        time.sleep(4)
        centralize()

def leave():
    left = False
    while not left:
        if exist('images\leave.png'):
            image_click('images\leave.png')
            time.sleep(4)
            
            break
        else:
            print('Leave button is not visible')
        time.sleep(1)


def chat():
    pass





    
   
