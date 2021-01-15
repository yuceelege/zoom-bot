import tkinter as tk
import tkinter.font as font
import pandas as pd
import numpy as np



class Window():
    def __init__(self,master):
        """
        Parameters
        ----------
        master : tkinter object
            the window that asks for schedule information

        """
        self.master = master
        master.title('Zoom Logger')
        master.geometry('800x600')
        
        myFont = font.Font(family='Helvetica', size=14, weight='bold')
        label1 = tk.Label(master,text='Enter Your Weekly Schedule',font=myFont) 
        label1.place(x =245,y =100)
        label2 = tk.Label(master,text='Course:') 
        label2.place(x =260,y =220)
        label3 = tk.Label(master,text='Day:') 
        label3.place(x =430,y =220)
        label3 = tk.Label(master,text='Start:') 
        label3.place(x =535,y =220)
        label3 = tk.Label(master,text='End:') 
        label3.place(x =615,y =220)
        label4 = tk.Label(master,text='Meeting ID:') 
        label4.place(x =110,y =360)
        label5 = tk.Label(master,text='Pwd:') 
        label5.place(x =250,y =360)
        label6 = tk.Label(master,text='Join Link:') 
        label6.place(x =615,y =360)
        
        entry1 = tk.Entry(master,fg='black',bg='white',width=20)
        entry1.place(x =205,y =250)
        entry2 = tk.Entry(master,fg='black',bg='white',width=8)
        entry2.place(x =520,y =250)
        entry3 = tk.Entry(master,fg='black',bg='white',width=8)
        entry3.place(x =600,y =250)
        entry4 = tk.Entry(master,fg='black',bg='white',width=13)
        entry4.place(x =390,y =250)
        
        entry5 = tk.Entry(master,fg='black',bg='white',width=13)
        entry5.place(x =100,y =400)
        entry6 = tk.Entry(master,fg='black',bg='white',width=9)
        entry6.place(x =230,y =400)
        entry7 = tk.Entry(master,fg='black',bg='white',width=28)
        entry7.place(x =540,y =400)
        
        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        c1 = tk.Checkbutton(master, text = "Option 1", variable = CheckVar1, onvalue = 1, offvalue = 0)
        c2 = tk.Checkbutton(master, text = "Option 2", variable = CheckVar2, onvalue = 1, offvalue = 0)
        c1.place(x = 190,y = 440)
        c2.place(x = 620,y = 440)
        
        def clear():
            """
            clears the whole entry bars

            Returns
            -------
            None.

            """
            entry1.delete(0,'end')
            entry2.delete(0,'end')
            entry3.delete(0,'end')
            entry4.delete(0,'end')
            entry5.delete(0,'end')
            entry6.delete(0,'end')
            entry7.delete(0,'end')
        
        data = []
        def add_value():
            """
            Adds the each lesson data to a temporary list when 'Add' is clicked.

            Returns
            -------
            bool

            """
            a = entry2.get().replace('.',':')
            b = entry3.get().replace('.',':')
            
            if (CheckVar2.get() == 1 and CheckVar1.get() == 1) or (CheckVar2.get() == 0 and CheckVar1.get() == 0):
                    print('WARNING: You have to choose only one of the boxes')
            if entry1.get() == "":
                print('WARNING: You have to fill the required boxes.')
                clear()
                return False
            elif entry2.get() == "":
                print('WARNING: You have to fill the required boxes.')
                clear()
                return False
            elif entry3.get() == "":
                print('WARNING: You have to fill the required boxes.')
                clear()
                return False
            elif entry4.get() == "":
                print('WARNING: You have to fill the required boxes.')
                clear()
                return False
            else:
                if CheckVar1.get() == 1:
                    if entry5.get() == "":
                        print('WARNING: You have to fill the required boxes.')
                        clear()
                        return False
                    elif entry6.get() == "":
                        print('WARNING: You have to fill the required boxes.')
                        clear()
                        return False
                    data.append(np.array([entry1.get(),a,b,entry4.get(),entry5.get()+'@xox@'+entry6.get()]))
                elif CheckVar2.get() == 1:
                    if entry7.get() == "":
                        print('WARNING: You have to fill the required boxes.')
                        clear()
                        return False
                    data.append(np.array([entry1.get(),a,b,entry4.get(),entry7.get()]))
            clear()
           
        def terminate():
            """
            Executed when 'Complete' button is clicked. Saves the all schedule to a csv file.
            Closes the schedule window.

            Returns
            -------
            None.

            """
            np.savetxt('data.csv',np.array(data),fmt='%s')
            master.destroy()
            
        button = tk.Button(master,text='Add', command = add_value)
        button.place(x =340,y =500)
        
        button2 = tk.Button(master,text='Complete', command = terminate)
        button2.place(x =405,y =500)
        
class Choice():
    def __init__(self,master,choice=None):
        """
        Parameters
        ----------
        master : tkinter object
            The first window where the user has two options start the bot/arrange the schedule.
        choice : TYPE, optional
        The default is None.

        Returns
        -------
        None.

        """
        self.master = master
        master.title('Welcome')
        master.geometry('280x50')
        def reset():
            """
            Arrange the schedule.
            Returns
            -------
            None.

            """
            self.choice = 0
            master.destroy()
        def start():
            """
            Start the bot.
            -------
            None.

            """
            self.choice = 1
            master.destroy()
   
        button3 = tk.Button(master,text='Change/Reset Schedule', command = reset)
        button3.place(x =0,y =0)
        
        button4 = tk.Button(master,text='Start the Bot', command = start)
        button4.place(x =185,y=0)
        
    def getchoice(self):
        """
        Get method for choice parameter

        Returns
        -------
        int
            binary representation of two options.

        """
        return self.choice
        
    
       
