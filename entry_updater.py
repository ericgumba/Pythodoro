PRODUCTIVITY_JOURNAL = "productivity-journal"

class EntryUpdater:

    def __init__(self, task:str = None): 
        self.task = task

    def updateEntry( self, entry, beginningAndEndOfEntry ): 

        beginningOfEntry, endOfEntry = beginningAndEndOfEntry[0], beginningAndEndOfEntry[1]
        assert beginningOfEntry > 0 and endOfEntry > 0 
        if self.task: 
            self.addPomodoroToEntry(beginningOfEntry)
            self.addPomodoroToTask()
        else:
            self.addPomodoroToEntry(beginningOfEntry)


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

    def addPomodoroToTask( self, data ): 

        for index, line in enumerate(data):
            if self.task in line: 
                data = self.addPomodoro(data, index)
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
        return open(PRODUCTIVITY_JOURNAL, 'r')
        