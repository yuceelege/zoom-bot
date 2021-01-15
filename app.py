from tools import *
import sys
import os.path


wait = True
while wait:
    try:
        pre = tk.Tk()
        page = interface.Choice(pre)
        pre.mainloop()
        if page.getchoice() == 0:
            initiate_schedule()
        elif page.getchoice() ==1:
            if os.path.exists("data.csv"):
                wait = False
            else:
                print('You have to add a schedule to start the bot.')

    except:
        sys.exit()
        

try:
    data = np.loadtxt('data.csv',dtype=np.str)
    if len(data.shape) == 1:
        data = np.array([data])
except:
    pass
    
flag = True
print('Session is started.')
counter = 0
while flag:
    try:
        for course in data:
            now = datetime.now()
            current_time =now.strftime("%H:%M")    
            if (now.weekday(),current_time) == exec_time(course[3],course[1]) and counter ==0:
                print('Signing in...')
                if course[4].find('@xox@') !=-1:
                    sign_in(course[4],False)
                    counter = 1
                else:
                    sign_in(False,course[4])
                    counter = 1
            elif (now.weekday(),current_time) == exec_time(course[3],course[2]) and counter ==1:
                centralize()
                time.sleep(0.8)
                print('Designatted time is over. Leaving...')
                leave()
                counter = 0
            
        
        time.sleep(5)
       
    except Exception:
        print('You have to type every day and hour with the correct format.')
        print('System Reseting. Fill the schedule again.')
        print('Notify us if the error is happened due to another reason.')
        try:
            os.remove('data.csv')
        except:
            pass
        sys.exit()
        
        



