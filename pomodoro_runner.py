import threading
import time  
from pomodoro import Pomodoro
import json 


class PomodoroRunner (threading.Thread):
    def __init__(self, threadID, name, cont, pomodoro: Pomodoro):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.cont = cont
        self.pomodoro = pomodoro

    def run(self):
        print ("Starting " + self.name +"\n")
        print ("waiting 2 seconds")
        time.sleep(2)
        while True: 
            if self.pomodoro.isWorking:
                time.sleep(25) 
                self.pomodoro.switchPomodoro()
                print("WRITING")
            else:
                time.sleep(5)
                self.pomodoro.switchPomodoro()
                print("BREAKING") 
cont = []

with open('settings.json') as json_file:
    settings = json.load(json_file) 

pom = Pomodoro(settings)



thread1 = PomodoroRunner(1, "Thread1", cont, pom)
 
thread1.start()