## Author : Rishita Ray , github : https://github.com/BlueCrimson976

import sys , os 
from tqdm.auto import tqdm
import time 
import emoji 
from playsound import playsound 
from colorama import Fore, Back, Style ,init
from ctypes import windll


init(autoreset=True)


## Write the program code 
def main():

  print(Fore.MAGENTA + 'Unpausable Timer 2 \n')
  print(Fore.RED + "Welcome to Unpausable Timer 2 \n")

  rules = ''' Rules : 

   1. You can't pause the timer , so be mindful to the time period you set yourself without getting out of your seat and be focused. Hence it's named Unpausable Timer. \n
   2. Inputs should all be Integers (No 0.5 , 1.5 etc) \n
   3. When You Resize the application use " Ctrl + '-' " for zooming out and press " Ctrl + '+' " for zooming out to get a neat visual representation. \n
   4. This application is built for focused studying and learning so , all these constraints are applied and minimalistic approach is taken , Don't feel hesistant if you can't finish a quest once, 
      Try to improve and embrace growth mindset! Also use time creativily to make the best use of it , \n
               
      Finally , Good Luck Explorer conquer the quest! \n \n '''

  print(Fore.GREEN + rules)  

  while True : ## Event loop (for continuous looping through the code)

    ringtone = 'loud_alarm_sound.wav'  
    print(Fore.LIGHTMAGENTA_EX + "New Quest :  \n")
    f = input(Fore.BLUE + 'Enter the Number of Rounds of the Quest : ')
    m = input(Fore.BLUE + 'Enter the Duration of each round in minutes : ')
    b = input(Fore.BLUE + 'Enter the Duration of break in minutes : ')  
    sys.stdout.write("\x1b[?7l")
    c = 0 ## pom counter
    t = int(m)*60 
    b = int(b)*60
    f = int(f)
    print(end='\n')
    for i in tqdm(range(f) , desc='Quest' , ncols=65 ,colour='GREEN' , leave=True):
        time.sleep(0.01)
        print(end = "\n")
        for j in tqdm(range(t) , desc=f'Round {i+1}' , ncols=55 ,colour='BLUE' ,leave=False):
            time.sleep(1) 
        playsound(ringtone)
        print(end='\n')
        print(emoji.emojize(Fore.BLUE + "Reward :tomato: \n"))
        c +=1 
        print('Pom Completed : ' , c)
        time.sleep(1)

        if (i+1 < f): 
          print('\n')
          print(emoji.emojize(Fore.MAGENTA + "Recharge :chocolate_bar: \n"))
          for k in tqdm(range(b) , desc=f'Break {i+1}' , ncols=45 ,colour='RED' , leave=False):
            time.sleep(1)
          print(end='\n')  
          time.sleep(2)
          playsound(ringtone)
          time.sleep(0.1)
          print(Fore.RED + "Break Ended ... Next Round Starts in 3s \n")
          time.sleep(3)  

        if (i+1==f):
            time.sleep(1)
            playsound(ringtone)
    print(emoji.emojize(Fore.YELLOW + " \n Congratulations You have completed the quest :trophy: \n "))     


# pass the commands you want to pass to cmd
if __name__ == '__main__':
    windll.shcore.SetProcessDpiAwareness(1)
    main()
