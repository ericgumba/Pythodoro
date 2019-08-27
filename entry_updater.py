PRODUCTIVITY_JOURNAL = "productivity-journal"

from journal_checker import JournalChecker              # dependencies that journal-writer.py relies on 

class EntryUpdater:

    def __init__(self, task:str = None): 
        self.task = task

    def updateEntry( self, entry, beginningAndEndOfEntry ): 

        beginningOfEntry, endOfEntry = beginningAndEndOfEntry[0], beginningAndEndOfEntry[1]
        data = self.obtainJournalData()

        assert beginningOfEntry > 0 and endOfEntry > 0 
        if self.task: 

            modifiedData = self.addPomodoro(data, beginningOfEntry-1)
            self.writeToJournal(modifiedData)

            if JournalChecker.taskInEntry(entry, data, self.task, beginningAndEndOfEntry):

                modifiedData = self.addPomodoroToTask(data, beginningAndEndOfEntry)
                self.writeToJournal(modifiedData)
            else:
                self.addTaskToEntry(entry, endOfEntry - 2)
        else:
            modifiedData = self.addPomodoro(data, beginningOfEntry-1)
            self.writeToJournal(modifiedData)

 
    def addPomodoroToTask( self, data, beginningAndEndOfEntry ): 
 

        for i in range(beginningAndEndOfEntry[0]+1, beginningAndEndOfEntry[1]):
            if self.task in data[i]:
                data = self.addPomodoro(data, i)
                return data

    def addPomodoro(self, data, index):


        data[index] = data[index].split(":")
        data[index][-1] = data[index][-1].strip() 
 
        data[index][-1] = str(int(data[index][-1]) + 1) + "\n"
        
        data[index+1] = data[index+1].rstrip() + "*" + "\n"

        data[index].insert(1,":")
        data[index] = "".join(data[index]) 

        return data

    def addEntryToJournal( self, entry, startingLine ):     
        data = self.obtainJournalData()
        data[startingLine] = '\n{}:0\n\n\n\n'.format(entry)
        self.writeToJournal(data)
 

    def addTaskToEntry(self, entry, endLine ):
        data = self.obtainJournalData() 
        data[endLine] = "      " + self.task + ":1\n" + "      " + "*\n\n\n" 
        self.writeToJournal(data)

    def obtainJournalData(self):
        with open(PRODUCTIVITY_JOURNAL, 'r') as file:  
            data = file.readlines()
        return data

    def writeToJournal(self, data):

        with open(PRODUCTIVITY_JOURNAL, 'w') as file:
            file.writelines( data )