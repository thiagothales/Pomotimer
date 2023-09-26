import time
import os
from plyer import notification



def pomotime(timee):

    clearscr = os.system("clear")
    cycles = 0
    
    timee = (timee * 60)
    reload_time = timee
    countdown = 5
    
    
    while countdown:
        minutes, seconds = divmod(countdown, 60)
        clock = '{:02d}:{:02d}' .format(minutes,seconds)
        print(clock,end='\r')
        time.sleep(1)
        countdown -=1
        
    for _ in range(0,4):
        
        notification.notify(
                title = "Pomotimer",
                message = "Let's go to work!"
            )   
        
        timee = reload_time
        while timee:
            clearscr
            minutes, seconds = divmod(timee, 60)
            clock = '{:02d}:{:02d}' .format(minutes,seconds)
            print("Time: " + clock,end='\r')
            time.sleep(1)
            timee -=1
            
        
        cycles += 1
        

        if cycles !=4:
            
            notification.notify(
                title = "Pomotimer",
                message = "Take a 5 minute break! You have completed a " + str(cycles) + " cycles."
            )
            
            rest_time = 300 #300 sec == 5 min
            
            while rest_time:
                
            
                minutes, seconds = divmod(rest_time, 60)
                clock = '{:02d}:{:02d}' .format(minutes,seconds)
                print("Rest: " + clock,end='\r')
                time.sleep(1)
                rest_time -=1
                    
            input("Press enter to next cycle...\r")        
            
            
    if cycles == 4 :
        notification.notify(
        title = "Pomotimer",
        message = "Good job! You have completed all cycles."
    )
      
        print(time.strftime("Pomodoro completed [%A - %d %B, %H:%M]")) 

            
def error_handling():
    try:
        timee = int(input('Insert your focus time in minutes: '))
        check_value = isinstance(timee,int)
        if check_value == True:
            pomotime(int(timee))

    except ValueError:
        print("\nIncorrect value type, insert a integer type value.\n")
        error_handling()
    except KeyboardInterrupt:
        print("\nYou has pressed Ctrl + C, the program was interrupt!\n")
        
error_handling()