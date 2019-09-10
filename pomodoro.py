import sys  
import os 
import sched
import threading
import time 
import journal_writer 
import json 
from productivity_journal_manager import ProductivityJournalManager
from productivity_journal_updater import ProductivityJournalUpdater


class Pomodoro:
    def __init__(self, settings, journalWriter: journal_writer.JournalWriter = journal_writer.JournalWriter(), productivityJournalManager: ProductivityJournalManager = ProductivityJournalManager(ProductivityJournalUpdater())):  
        self.workDuration = settings["workDurationInMinutes"]
        self.breakDuration = settings["breakDurationInMinutes"]
        self.pomodoroStamp = settings["pomodoroStamp"]
        self.isWorking = True
        self.journalWriter = journalWriter
        self.productivityJournalManager = productivityJournalManager
        self.minutesElapsed = 0
         
    def writeToJournal(self): 
        self.journalWriter.write(self.pomodoroStamp) 
    
    def updateTotal(self):
        self.journalWriter.updateTotalTimeWorked()
        self.productivityJournalManager.updateProductivityJournal()

    def switchPomodoro(self):  
        if self.isWorking:
            self.isWorking = False 
        else: 
            self.isWorking = True 

    # def runPomodoroMode(self): 
    #     minute = 10 # seconds

    #     if self.isWorking: 

    #         while self.minutesElapsed < self.workDuration:
    #             time.sleep(minute)
    #             self.minutesElapsed += 1
    #             print(str(self.minutesElapsed) + " out of " + str(self.workDuration) + " minutes elapsed for work." )
    #             self.updateTotal()

    #         self.switchPomodoro()
    #         print("writing to journal and taking break")

    #     else:
    #         while self.minutesElapsed < self.breakDuration:
    #             time.sleep(minute)
    #             self.minutesElapsed += 1
    #             print(str(self.minutesElapsed) + " out of " + str(self.breakDuration) + " minutes elapsed for break." )
                
    #         self.switchPomodoro() 
    #         print("Going back to work") 