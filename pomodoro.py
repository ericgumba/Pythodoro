import sys  
import os 
import sched
import threading
import time 
import journal_writer 
import json 

class Pomodoro:
    def __init__(self, settings, journalWriter: journal_writer.JournalWriter = journal_writer.JournalWriter()):  
        self.workDuration = settings["workDurationInMinutes"] * 60
        self.breakDuration = settings["breakDurationInMinutes"] * 60
        self.soundOn = settings["soundOn"]
        self.pomodoroModeOn = settings["pomodoroModeOn"] 
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
             