import sys  
import os 
import sched
import threading
import time 
import journal_writer 
import json 

class Pomodoro:
    def __init__(self, settings, journalWriter: journal_writer.JournalWriter = journal_writer.JournalWriter()):  
        self.workDuration = settings["workDuration"]
        self.breakDuration = settings["breakDuration"]
        self.soundOn = settings["soundOn"]
        self.pomodoroModeOn = settings["pomodoroModeOn"] 
        self.isWorking = True
        self.journalWriter = journalWriter
         
    def writeToJournal(self): 
        journalWriter.write() 

    def switchPomodoro(self):  
        if self.isWorking:
            self.isWorking = False
        else: 
            self.isWorking = True
            journalWriter.write() 
 
 