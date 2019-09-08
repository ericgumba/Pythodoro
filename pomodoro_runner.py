import threading
import time  
from pomodoro import Pomodoro
import json 
import sys
from journal_writer import JournalWriter
from productivity_journal_manager import ProductivityJournalManager
from productivity_journal_updater import ProductivityJournalUpdater
import os

class PomodoroRunner (threading.Thread):
    def __init__(self, threadID, name, pomodoro: Pomodoro):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name 
        self.pomodoro = pomodoro

     

    def run(self):
        print ("Starting " + self.name +"\n") 
        while True:  
            self.pomodoro.runPomodoroMode()
 
 


 
if __name__ == "__main__":

    with open('settings.json') as json_file:
        settings = json.load(json_file) 
         
    if len(sys.argv) > 1:
        task = sys.argv[1]
        journalWriter = JournalWriter(task)
        productivityJournalManager = ProductivityJournalManager(task)
    else:
        journalWriter = JournalWriter()
        productivityJournalManager = ProductivityJournalManager()

    pom = Pomodoro(settings, journalWriter, productivityJournalManager) 
 
    pomodoroThread = PomodoroRunner(1,"Thread1", pom) 
    pomodoroThread.start()