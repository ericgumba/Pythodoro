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

    def addPomodoroToTask(self):
        print("implement addPomodoroToTask")
        print("DOING IT NOW")