PRODUCTIVITY_JOURNAL = "productivity-journal"

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

            modifiedData = self.addPomodoroToTask(data, beginningAndEndOfEntry)
            self.writeToJournal(modifiedData)
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
        data[index+1] = "*" + data[index+1]

        data[index].insert(1,":")
        data[index] = "".join(data[index]) 

        return data

    def obtainJournalData(self):
        with open(PRODUCTIVITY_JOURNAL, 'r') as file:  
            data = file.readlines()
        return data

    def writeToJournal(self, data):

        with open(PRODUCTIVITY_JOURNAL, 'w') as file:
            file.writelines( data )


a = EntryUpdater()

a.updateEntry("all-time", (1,14))