

import date 
from journal_checker import JournalChecker              # dependencies that journal-writer.py relies on 
import entry_updater
from journal import Journal

from total_time_updater import TotalTimeUpdater
# Write sequence of lines at the end of the file.


#Note about the function g
class JournalWriter:
    def __init__(self, task:str = None): 
        self.task = task
        Journal.initializeJournal(date.getCurrentDate())
        if self.task:
            self.entryUpdater = entry_updater.EntryUpdater (task)
        else:
            self.entryUpdater = entry_updater.EntryUpdater(task)

    def updateTotalTimeWorked(self):
        data = Journal.obtainJournalData()

        updatedData = TotalTimeUpdater.updateTotal(data)

        Journal.writeToJournal(updatedData)

        
    def write(self, pomodoroStamp): 
        self.writeToEntry("all-time", pomodoroStamp)

        curDate = date.getCurrentDate()
        self.writeToEntry(curDate, pomodoroStamp) 

    def writeToEntry(self, entry:str, pomodoroStamp):   

        assert entry == "all-time" or entry == date.getCurrentDate(), "Time is not valid"
        if JournalChecker.inJournal(entry):
            beginningAndEndOfEntry = JournalChecker.getBeginningAndEndOfEntry(entry)
            self.entryUpdater.updateEntry(entry, beginningAndEndOfEntry, pomodoroStamp ) 
 
        else:
            startingLine = JournalChecker.getBeginningAndEndOfEntry("all-time")[1]
            self.entryUpdater.addEntryToJournal( entry, startingLine-1 )
            beginningAndEndOfEntry = JournalChecker.getBeginningAndEndOfEntry(entry)
            self.entryUpdater.updateEntry( entry, beginningAndEndOfEntry, pomodoroStamp )
              