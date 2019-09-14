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
import sound
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
            if self.pomodoro.getTask() is None:
                print("YOU ARE CURRENTLY WORKING: (TASK UNSPECIFIED)" )
                print(str(self.minutesElapsed) + " minutes complete out of " + str(self.pomodoro.workDuration))

            else: 
                print("YOU ARE CURRENTLY WORKING ON: " + self.pomodoro.getTask())
                print(str(self.minutesElapsed) + " minutes complete out of " + str(self.pomodoro.workDuration))
        else:

            print("YOU ARE CURRENTLY TAKING A BREAK")
            print( str( self.minutesElapsed ) + " minutes complete out of " + str(self.pomodoro.breakDuration))
    
    def incrementMinute(self):
    
        self.minutesElapsed += 1
        self.secondsElapsed = 0
    
    def skipCurrentSession(self):
        
        s = "WORK" if self.pomodoro.isWorking else "BREAK"

        print("SKIPPING {} CURRENT SESSION".format(s))
         
        # if at least half of the session is complete, reward a stamp anyways.
        if self.minutesElapsed >= self.pomodoro.workDuration/2:
            self.pomodoro.writeToJournal()

        self.pomodoro.switchPomodoro()
        self.resetTimer() 





    def run(self, r):

        def runProductivityTracker():
            minute = 60 # seconds

            time.sleep(1)
            self.secondsElapsed += 1

            if self.secondsElapsed >= minute:
                self.pomodoro.updateTotal()
                self.resetTimer()

        def runPomodoro(): 
            minute = 60 # seconds 
            if self.pomodoro.isWorking:  
                if self.pomodoro.workDuration <= self.minutesElapsed: 
                    self.pomodoro.writeToJournal() 
                    self.pomodoro.switchPomodoro()
                    sound.playBreakSound()
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
                    sound.playWorkSound()

                    



                else: # keep incrementing minutes elapsed

                    time.sleep(1)
                    self.secondsElapsed +=1

                    if self.secondsElapsed >= minute:
                        self.minutesElapsed += 1
                        self.secondsElapsed = 0
                        self.printCurrentSessionStats()

 
        while True:  
            if r.value == 1: 
                if self.pomodoro.pomodoroModeOn:
                    runPomodoro()
                else:
                    runProductivityTracker()
            elif r.value == 2:
                self.skipCurrentSession()
                r.value = 1
            else:  
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
    END = "end"
    TASK = "task"
    pausePlaySkip = [PLAY] # this actually doesnt need to be a queue, but perhaps one day
    while True:  
        command = str(input("Type 'pause', 'play', 'skip' or 'end' and [Enter] to pause the pomodoro, resume, skip, or end the current session\n"))
          
        
        if command.lower() == PLAY:
            if pausePlaySkip[-1].lower() == PAUSE:
                print("Resuming Pomodoro")
                run.value = not run.value
                pausePlaySkip.pop()
                pausePlaySkip.append(command)
            else:
                print("POMODORO IS ALREADY PLAYING")

        elif command.lower() == PAUSE:
            if pausePlaySkip[-1].lower() == PLAY: 
                print("Pausing Pomodoro")
                run.value = not run.value
                pausePlaySkip.pop()
                pausePlaySkip.append(command)
            else:
                print("POMODORO IS ALREADY PAUSED")

        elif command.lower() == SKIP:
            #IMPLEMENT SKIP! 
            run.value = 2
        elif command.lower() == TASK:
            print(JournalWriter.task)
        elif command.lower() == END:
            p.terminate()
            print("ENDING SESSION")
            break 
        else:
            print('INVALID COMMAND \n')