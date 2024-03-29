 

from .journal_checker import JournalChecker              # dependencies that journal-writer.py relies on 

from .journal import Journal
class EntryUpdater:

    def __init__(self, task:str = None): 
        self.task = task

    def updateEntry( self, entry, beginningAndEndOfEntry, stamp ): 

        beginningOfEntry, endOfEntry = beginningAndEndOfEntry[0], beginningAndEndOfEntry[1]
        data = Journal.obtainJournalData()

        assert beginningOfEntry > 0 and endOfEntry > 0 
        if self.task: 

            modifiedData = self.addPomodoro(data, beginningOfEntry, stamp)
            self.writeToJournal(modifiedData)

            if JournalChecker.taskInEntry(entry, data, self.task, beginningAndEndOfEntry):

                modifiedData = self.addPomodoroToTask(data, beginningAndEndOfEntry, stamp)
                self.writeToJournal(modifiedData)
            else:
                self.addTaskToEntry(entry, endOfEntry - 1)
        else:
            modifiedData = self.addPomodoro(data, beginningOfEntry, stamp)
            self.writeToJournal(modifiedData)

 
    def addPomodoroToTask( self, data, beginningAndEndOfEntry, stamp ): 
 

        for i in range(beginningAndEndOfEntry[0]+1, beginningAndEndOfEntry[1]):
            if self.task in data[i]:
                data = self.addPomodoro(data, i, stamp)
                return data

    def addPomodoro(self, data, index, stamp):


        data[index] = data[index].split(":")
        data[index][-1] = data[index][-1].strip() 
 
        data[index][-1] = str(int(data[index][-1]) + 1) + "\n"
        
        data[index+1] = data[index+1].rstrip() + stamp + "\n"

        data[index].insert(1,":")
        data[index] = "".join(data[index]) 

        return data

    def addEntryToJournal( self, entry, startingLine ):     
        data = Journal.obtainJournalData()
        data[startingLine] = '\n{}:0\n\n\n\n'.format(entry)
        Journal.writeToJournal(data)
 

    def addTaskToEntry(self, entry, endLine ):
        data = Journal.obtainJournalData() 
        data[endLine] = "      " + self.task + ":1\n" + "      " + "*\n\n\n" 
        Journal.writeToJournal(data)
 

    def writeToJournal(self, data): 
        Journal.writeToJournal(data)