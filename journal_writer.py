PRODUCTIVITY_JOURNAL = "productivity-journal"

import date 
from journal_checker import JournalChecker              # dependencies that journal-writer.py relies on
from entry_writer import EntryWriter                    # to write to productivity-journal
import entry_updater
# Write sequence of lines at the end of the file.


#Note about the function g
class JournalWriter:
    def __init__(self, task:str = None): 
        self.task = task
        self.entryUpdater = entry_updater.EntryUpdater(task)
        
    def write(self): 
        self.writeToEntry("all-time")
        self.writeToEntry(date.getCurrentDate()) 

    def writeToEntry(self, entry:str):   

        assert entry == "all-time" or entry == date.getCurrentDate(), "Time is not valid"
        if JournalChecker.inJournal(entry):
            self.entryUpdater.updateEntry(entry, JournalChecker.getBeginningAndEndOfEntry(entry)) 
        else:
            startingLine = JournalChecker.getBeginningAndEndOfEntry("all-time")[1]
            EntryWriter.addEntryToJournal( entry, startingLine-2 )
             
 



    def addPomodoroToTask(self):
        print("Implement addpomodoroToTask")

        




a = JournalWriter()

a.write()




# with is like your try .. finally block in this case


# print data
# print "Your name: " + data[0]

# # now change the 2nd line, note that you have to add a newline
# data[1] = 'Mage\n'

# # and write everything back
# with open('stats.txt', 'w') as file:
#     file.writelines( data )