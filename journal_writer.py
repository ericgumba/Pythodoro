PRODUCTIVITY_JOURNAL = "productivity-journal"

import date 
from journal_checker import JournalChecker
from entry_writer import EntryWriter
# Write sequence of lines at the end of the file.


#Note about the function getBeginningAndEndOfEntry 
class JournalWriter:
    def __init__(self, task:str = None): 
        self.task = task
        
    def write(self): 
        self.writeToEntry("all-time")
        self.writeToEntry(date.getCurrentDate()) 

    def writeToEntry(self, entry:str):   

        assert entry == "all-time" or entry == date.getCurrentDate(), "Time is not valid"
        if JournalChecker.inJournal(entry):
            self.updateEntry(entry) 
        else:
            EntryWriter.addEntryToJournal( entry, JournalChecker.getBeginningAndEndOfEntry(entry) )
            
    def addEntryToJournal(self, entry):   
        startingLine = JournalChecker.getBeginningAndEndOfEntry(entry)[1] - 2
        with open(PRODUCTIVITY_JOURNAL, 'r') as file: 
            data = file.readlines()
 

        data[startingLine] = '\n{}:1 \n \n \n'.format(entry)

        # and write everything back
        with open(PRODUCTIVITY_JOURNAL, 'w') as file:
            file.writelines( data )
 


    def updateEntry(self, entry):
        beginning, end = JournalChecker.getBeginningAndEndOfEntry(entry)

        assert beginning > 0 and end > 0
        print(beginning, end)
        if self.task:
            print("Task {} exists, so update task".format(self.task))
            self.addPomodoroToEntry(beginning)
            self.addPomodoroToTask()
        else:
            self.addPomodoroToEntry(beginning)

    def addPomodoroToEntry(self,beginning):

        print("Implement addPomodoroToEntry")
        with open(PRODUCTIVITY_JOURNAL, 'r') as file: 
            print("BEG", beginning)
            data = file.readlines()
 

        data[beginning-1] = data[beginning-1].split(":")
        data[beginning-1][-1] = data[beginning-1][-1].strip()
        data[beginning] = data[beginning].strip() 
 
        data[beginning-1][-1] = str(int(data[beginning-1][-1]) + 1) + "\n"
        data[beginning] += "*\n"

        data[beginning-1].insert(1,":")
        data[beginning-1] = "".join(data[beginning-1]) 

        with open(PRODUCTIVITY_JOURNAL, 'w') as file:
            file.writelines( data )

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