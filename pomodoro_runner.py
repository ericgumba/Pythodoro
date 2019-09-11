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
    
    def skipCurrentSession(self):
        print("SSKIPPING", self.minutesElapsed)
        print(self.secondsElapsed)
        
        # if at least half of the session is complete, reward a stamp anyways.
        if self.minutesElapsed > self.pomodoro.workDuration/2:
            self.pomodoro.writeToJournal()

        self.pomodoro.switchPomodoro()
        self.resetTimer() 





    def run(self, r):
        def runPomodoro(): 
            minute = 60 # seconds 
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
            if r.value == 1: 
                runPomodoro()
            elif r.value == 2:
                self.skipCurrentSession()
                r.value = 1
            else: 
                print("PAUSED")
                time.sleep(1)
 
 


 
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
    

    p = Process(target=pomodoroThread.run, args=(run,)) 
    p.start() 
    
    
    # listens for input. Which will pause the PomodoroRunner, skip to next session or continue from pause state
    PAUSE = "pause"
    PLAY = "play"
    SKIP = "skip"
    
    pausePlaySkip = [PLAY] # this actually doesnt need to be a queue, but perhaps one day
    while True:  
        command = str(input("Type 'pause', 'play' or 'skip' to pause the pomodoro, resume, or skip the current session\n "))
          
        
        if command.lower() == PLAY:
            if pausePlaySkip[-1].lower() == PAUSE:
                print("REST")
                run.value = not run.value
                pausePlaySkip.pop()
                pausePlaySkip.append(command)
            else:
                print("POMODORO IS ALREADY PLAYING")

        elif command.lower() == PAUSE:
            if pausePlaySkip[-1].lower() == PLAY:
                print("TEST")
                run.value = not run.value
                pausePlaySkip.pop()
                pausePlaySkip.append(command)
            else:
                print("POMODORO IS ALREADY PAUSED")

        elif command.lower() == SKIP:
            #IMPLEMENT SKIP! 
            run.value = 2

        else:
            print("Invalid command\n")
            
