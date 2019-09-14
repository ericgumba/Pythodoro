import sys  
import os 
import sched
import threading
import time 
from .journal_writer import JournalWriter
import json 
from .productivity_journal_manager import ProductivityJournalManager
from .productivity_journal_updater import ProductivityJournalUpdater
from .journal_writer import JournalWriter


class Pomodoro:
    def __init__(self, settings, journalWriter: JournalWriter = JournalWriter(), productivityJournalManager: ProductivityJournalManager = ProductivityJournalManager(ProductivityJournalUpdater())):  
        self.workDuration = settings["workDurationInMinutes"]
        self.breakDuration = settings["breakDurationInMinutes"]
        self.pomodoroStamp = settings["pomodoroStamp"]
        self.pomodoroModeOn = settings["pomodoroModeOn"]
        self.isWorking = True
        self.journalWriter = journalWriter
        self.productivityJournalManager = productivityJournalManager
        self.minutesElapsed = 0
         
    def writeToJournal(self): 
        self.journalWriter.write(self.pomodoroStamp) 
    
    def updateTotal(self):
        self.journalWriter.updateTotalTimeWorked()
        self.productivityJournalManager.updateProductivityJournal()

    def getTask(self):
        return self.journalWriter.task
        
    def switchPomodoro(self):  
        if self.isWorking:
            self.isWorking = False 
        else: 
            self.isWorking = True 


if __name__ == "__main__":
    j = JournalWriter("love")
 
    pm = ProductivityJournalManager("love")



    with open('settings.json') as json_file:
        settings = json.load(json_file) 
    pom = Pomodoro(settings, j, pm)

    pom.updateTotal()
