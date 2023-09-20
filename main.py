import time
from plyer import notification



def pomotime(timee):

    cycles = 0
    
    timee = 5
    reload_time = timee
    
    for cycles in range(0,4):
        
        notification.notify(
                title = "Pomotimer",
                message = "Let's go to work!"
            )   
        
        
        timee = reload_time
        while timee:
            minutes, seconds = divmod(timee, 60)
            clock = '{:02d}:{:02d}' .format(minutes,seconds)
            print(clock,end='\r')
            time.sleep(1)
            timee -=1
            
        
        cycles += 1
        

        if cycles !=4:
            
            notification.notify(
                title = "Pomotimer",
                message = "Take a 5 minute break! You have completed a " + str(cycles) + " cycles."
            )
            
            rest_time = 10 #300 sec == 5 min
            
            while rest_time:
                
            
                minutes, seconds = divmod(rest_time, 60)
                clock = '{:02d}:{:02d}' .format(minutes,seconds)
                print(clock,end='\r')
                time.sleep(1)
                rest_time -=1
                    
            input("Press enter to next cycle...\r")        
            
            
    if cycles == 4 :
        notification.notify(
        title = "Pomotimer",
        message = "Good job! You have completed all cycles."
    )
      
        print(time.strftime("Pomodoro completed [%A - %d %B, %H:%M]")) 

            
timee = input('Insert your focus time in minutes: ')
pomotime(int(timee))