# zoom-bot (BETA)
I built a zoom bot that will automatically log in and log out according the given schedule

## Prerequisite External Libraries
-Tkinter <br/>
-Pyautogui <br/>
-Pandas <br/>
-Numpy <br/>
-Subprocess <br/>
-webbrowser

## INFO
In order to start the program, **app.py** must be initialized.

## Method
-The program starts by displaying a window that offers two operations: Change Schedule / Start the Bot <br/>
-If first one is chosen, first window will close and another will open, asking for the lessons in schedule and required information. <br/>
-Once you wrote the required information and access information (choose and write only one type of access info), click add to put more lessons. <br/>
-Once you finish adding your weekly lessons, click 'Complete' and the program will return to first window. <br/>
-You can then start the bot.  <br/>
-If microphone and camera are opened, the bot will mute itself and close the camera to eliminate any unwanted scenario.

## WARNING
Don't touch the mouse or type with keyboards while the bot is operating because it uses GUI as input system.

## WARNING
Don't speak loudly while the bot enters the room because it uses image recogintion to identify microphone for muting <br/>
but if you speak loudly, microphone will become green and that might cause problems.

## WARNING
In the **tools.py** file line 122, you see that the fullscreen method is a little bit primitive. You may need to change the value 170 according to your screen
resolution; however, I am working on that and will fix soon. Also this is still the BETA version; therefore, I hope for your tolerance. <br/>

## WARNING
Don't delete the Zoom.lnk file, shortcut of the Zoom.exe is necessary for the program.

Other than that, Enjoy :)




