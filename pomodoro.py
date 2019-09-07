import sys  
import os 
import sched
import threading
import time 
import journal_writer 
import json 

class Pomodoro:
    def __init__(self, settings, journalWriter: journal_writer.JournalWriter = journal_writer.JournalWriter()):  
        self.workDuration = settings["workDurationInMinutes"]
        self.breakDuration = settings["breakDurationInMinutes"]
        self.pomodoroStamp = settings["pomodoroStamp"]
        self.isWorking = True
        self.journalWriter = journalWriter
         
    def writeToJournal(self): 
        self.journalWriter.write(self.pomodoroStamp) 
    
    def updateTotal(self):
        self.journalWriter.updateTotalTimeWorked()

    def switchPomodoro(self):  
        if self.isWorking:
            self.isWorking = False
            self.journalWriter.write(self.pomodoroStamp)
        else: 
            self.isWorking = True 

    def runPomodoroMode(self):
        minutesElapsed = 0
        minute = 1

        if self.isWorking: 

            while minutesElapsed < self.workDuration:
                time.sleep(minute)
                minutesElapsed += 1
                print(str(minutesElapsed) + " out of " + str(self.workDuration) + " minutes elapsed for work." )
                self.updateTotal()

            self.switchPomodoro()
            print("writing to journal and taking break")

        else:
            while minutesElapsed < self.breakDuration:
                time.sleep(minute)
                minutesElapsed += 1
                print(str(minutesElapsed) + " out of " + str(self.breakDuration) + " minutes elapsed for break." )
                
            self.switchPomodoro() 
            print("Going back to work") 