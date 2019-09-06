import threading
import time  
from pomodoro import Pomodoro
import json 
import sys
from journal_writer import JournalWriter
import os

class PomodoroRunner (threading.Thread):
    def __init__(self, threadID, name, pomodoro: Pomodoro):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name 
        self.pomodoro = pomodoro

    def runPomodoroMode(self):
        minutesElapsed = 0
        minute = 60

        if self.pomodoro.isWorking: 

            while minutesElapsed < self.pomodoro.workDuration:
                time.sleep(minute)
                minutesElapsed += 1
                self.pomodoro.updateTotal()

            self.pomodoro.switchPomodoro()
            print("writing to journal and taking break")

        else:
            while minutesElapsed < self.pomodoro.breakDuration:
                time.sleep(minute)
                minutesElapsed += 1
                
            self.pomodoro.switchPomodoro() 
            print("Going back to work") 
    
    def runPomodoroWithoutBreaks(self):

    def run(self):
        print ("Starting " + self.name +"\n") 
        while True:  
            self.runPomodoroMode()
 
 


 
if __name__ == "__main__":

    with open('settings.json') as json_file:
        settings = json.load(json_file) 
         
    if len(sys.argv) > 1:
        task = sys.argv[1]
        journalWriter = JournalWriter(task)
    else:
        journalWriter = JournalWriter()

    pom = Pomodoro(settings, journalWriter)
    pom.writeToJournal()
    pomodoroThread = PomodoroRunner(1,"Thread1", pom) 
    pomodoroThread.start()