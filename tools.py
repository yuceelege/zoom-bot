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
    """
    Executes the schedule arrangement window

    Returns
    -------
    None.

    """
    root = tk.Tk()
    page = interface.Window(root)
    root.mainloop()

def exec_time(day,time):
    """
    Converts the input strings into date

    Parameters
    ----------
    day : str
    
    time : str
        hour and minute.

    Returns
    -------
    tuple
        date
    """
    days= ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    try:
        return (days.index(day.lower()),time)
    except:
        print('You have to type the day correctly. Start Again :(')
        os.remove('data.csv')
        sys.exit()


def exist(image):
    """
    Check if the required image exists on the screen

    Parameters
    ----------
    image : str
        location of the image file.

    Returns
    -------
    bool
        exists or not.
    """
    try:
        if len(pyautogui.locateCenterOnScreen(image)) == 2:
            return True
    except Exception:
        return False
    
def centralize():
    """
    Brings the mouse to middle of the page to make buttons on the bottom
    of zoom program visible again because they disappear if the screen is not
    touched.

    Returns
    -------
    None.

    """
    x = pyautogui.size()
    pyautogui.moveTo(x[0]//2, x[1]//2)
    time.sleep(0.1)
    pyautogui.moveTo(500, 500)


def image_click(file):
    """
    Clicks the image

    Parameters
    ----------
    file : str
        location of the image file.

    Returns
    -------
    iconX : int
        x-coordinate
    iconY : int
        y-coordinate

    """
    iconX, iconY = pyautogui.locateCenterOnScreen(file)
    pyautogui.click(iconX, iconY)
    return iconX, iconY

def full_screen():
    """
    Makes the zoom program fullscreen

    Returns
    -------
    None.

    """
    time.sleep(2)
    if exist('images\full_screen.png'):
        iconX, iconY = pyautogui.locateCenterOnScreen('images\full_screen.png')
        pyautogui.click(iconX+170, iconY)
        

def sign_in(credential=False,link=False):
    """
    Sign in the zoom session.
    It considers both type of signing in (with link, with ID)

    Parameters
    ----------
    credential : TYPE, optional
         The default is False.
    link : TYPE, optional
         The default is False.

    Returns
    -------
    bool
        

    """
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
    """
    Leaves the session

    Returns
    -------
    None.

    """
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





    
   
