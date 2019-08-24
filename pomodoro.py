import sys  
import os 
import sched
import threading
import time 
import journal_writer




 


# Write sequence of lines at the end of the file.

class Pomodoro:
    def __init__(self, task = None):
        self.isWorking = True
        self.task = task
        self.journalWriter = journal_writer.JournalWriter(task)
         
    def writeToJournal(self): 
        journalWriter.write()

    def getBackToWork(self):
        print("back to work")



    def switchPomodoro(self):  
        if self.isWorking:
            self.takeABreak()
        else: 
            self.work()

    def work(self):
        self.isWorking = not self.isWorking
        self.writeToJournal()


    def takeABreak(self): 
        self.isWorking = True
        self.getBackToWork()

  


def startPomodoro():
    if pom.isWorking:  
        pom.switchPomodoro() 
        # os.system('say "break time."')  
    else:
        pom.switchPomodoro()
        # os.system('say "back to work."')

pom = Pomodoro("Love")


# need help with thread. Basically I've started a thread, however I end up getting a stack overflow. I've tried 

# run interleaving threads. Once first thread is complete, second one starts. Once second thread starts, first thread starts again.



def pomodoroStart( workDuration ):        
    count = 0
    while count < workDuration:
       time.sleep(1)
       count += 1
    if pom.isWorking:
        pom.switchPomodoro()
        os.system( 'say "break time."' )
    else:
        os.system( 'say "back to work"' ) 
        pom.switchPomodoro()


def startThread():
    while True:
    	pomodoroStart( 25 )
    	pomodoroStart( 5  )

startThread()