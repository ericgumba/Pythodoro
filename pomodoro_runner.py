import threading
import time  
from pomodoro import Pomodoro
import json 
import sys
from journal_writer import JournalWriter
from productivity_journal_manager import ProductivityJournalManager
from productivity_journal_updater import ProductivityJournalUpdater
import os
from multiprocessing import Process, Value 

class PomodoroRunner:
    def __init__(self, pomodoro: Pomodoro): 
        self.pomodoro = pomodoro
        self.minutesElapsed = 0
        self.secondsElapsed = 0

    def resetTimer(self):
        self.secondsElapsed = 0
        self.minutesElapsed = 0

    def printCurrentSessionStats(self):

        if self.pomodoro.isWorking:
            print("YOU ARE CURRENTLY WORKING:")
            print(str(self.minutesElapsed) + " minutes complete out of " + str(self.pomodoro.workDuration))
        else:
            print("YOU ARE CURRENTLY TAKING A BREAK")
            print( str( self.minutesElapsed ) + " minutes complete out of " + str(self.pomodoro.breakDuration))
    
    def incrementMinute(self):
    
        self.minutesElapsed += 1
        self.secondsElapsed = 0
    
    
    def run(self, r):
        def runPomodoro(): 
            minute = 2 # seconds 
            if self.pomodoro.isWorking:  
                if self.pomodoro.workDuration <= self.minutesElapsed: 
                    self.pomodoro.writeToJournal() 
                    self.pomodoro.switchPomodoro()

                    # reset minute and second
                    self.resetTimer()


                else: 

                    # increment second
                    time.sleep(1)
                    self.secondsElapsed += 1

                    
                    
                    if self.secondsElapsed >= minute:

                        # after we increment minute, we update total in journal
                        self.minutesElapsed += 1 
                        self.pomodoro.updateTotal()
                        self.secondsElapsed = 0
                        self.printCurrentSessionStats()

            else: # pomodoro is in not work mode


                #Check to see if break is over
                if self.pomodoro.breakDuration <= self.minutesElapsed:
                    
                    # if break is over, then we switch pomodoro state, and reset minutes and seconds elapsed
                    self.pomodoro.switchPomodoro()
                    self.resetTimer()

                    



                else: # keep incrementing minutes elapsed

                    time.sleep(1)
                    self.secondsElapsed +=1

                    if self.secondsElapsed >= minute:
                        self.minutesElapsed += 1
                        self.secondsElapsed = 0
                        self.printCurrentSessionStats()

 
        while True:  
            if r.value: 
                runPomodoro()
            else:
                print("pausing this shit")
                time.sleep(5)
 
 


 
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
 
    pomodoroThread = PomodoroRunner(pom)
 
    run = Value("i", 1) 
    print("RUN VALUE    ", run)

    p = Process(target=pomodoroThread.run, args=(run,)) 
    p.start() 

    
    # listens for input. Which will pause the PomodoroRunner, skip to next session or continue from pause state
    PAUSE = "pause"
    PLAY = "play"
    SKIP = "skip"
    
    pausePlaySkip = [PLAY]
    while True:  
        command = str(input("Type 'pause', 'play' or 'skip' to pause the pomodoro, resume, or skip the current session "))
         
        s = ""
        
        if pausePlaySkip[-1].lower() == PAUSE and command == PLAY:
            print("REST")
            run.value = not run.value

        elif pausePlaySkip[-1].lower() == PLAY and command == PAUSE:
            print("TEST")
            run.value = not run.value
        
