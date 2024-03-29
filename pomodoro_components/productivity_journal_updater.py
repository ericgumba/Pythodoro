from .date import date
from .productivity_journal_checker import ProductivityJournalChecker
from .productivity_journal import ProductivityJournal

TIME_IN_MINUTES = "total-minutes-worked:0"
TIME_IN_HOURS = "total-hours-worked:0"
class ProductivityJournalUpdater:
    def __init__(self, task = None): 
        self.task = task
        curDate = date.getCurrentDate()
        ProductivityJournal.initializeJournal(curDate)

    def update(self):

        curDate = date.getCurrentDate()

        self.updateTotalTime("all-time")

        if ProductivityJournalChecker.inJournal(curDate):
            self.updateTotalTime(curDate)
        else:
            self.createNewEntry(curDate)
            self.updateTotalTime(curDate)

    def updateTotalTime(self, entry):
        beginningAndEndOfEntry = ProductivityJournalChecker.getBeginningAndEndOfEntry(entry)
        data = ProductivityJournal.obtainJournalData()

        if self.task:
            if not ProductivityJournalChecker.taskInEntry(entry, data, self.task, beginningAndEndOfEntry):
                self.createNewTaskInEntry(entry) 
        
        self.updateEntry(entry) 

    def createNewEntry(self, entry):
        data = ProductivityJournal.obtainJournalData()

        FIRST_ENTRY = "all-time"

        _, endOfEntry = ProductivityJournalChecker.getBeginningAndEndOfEntry(FIRST_ENTRY)

        oneLine = 1
        data[endOfEntry - oneLine] = "\n" + entry + "\n" + TIME_IN_MINUTES + "\n" + TIME_IN_HOURS +  "\n\n\n"

        ProductivityJournal.writeToJournal(data)


    def createNewTaskInEntry(self, entry): 
        # data
        assert self.task is not None, " ERROR, TASK NOT SPECIFIED FOR PRODUCTIVITY JOURNAL UDPATER"
        data = ProductivityJournal.obtainJournalData()

        startOfEntry, endOfEntry = ProductivityJournalChecker.getBeginningAndEndOfEntry(entry)

        oneLine = 1

        data[endOfEntry - oneLine] = "    " + self.task + "\n" + "    " + TIME_IN_MINUTES + '\n' + "    " + TIME_IN_HOURS + '\n\n\n'

        ProductivityJournal.writeToJournal(data) 

    def updateEntry(self, entry): 

        
        indexOfEntry, indexEnd = ProductivityJournalChecker.getBeginningAndEndOfEntry(entry)
        data = ProductivityJournal.obtainJournalData()

        self.updateEntryTime(indexOfEntry)

        if self.task: 
            indexOfTask = ProductivityJournalChecker.getIndexOfTask(indexOfEntry, indexEnd, self.task)
            self.updateEntryTime( indexOfTask)

    def updateTaskInEntry(self, entry):

        print('h')

    def updateEntryTime(self, indexOfEntry):
        totalMinutes = indexOfEntry+1
        totalHours = indexOfEntry+2

        data = ProductivityJournal.obtainJournalData() 


        data[totalMinutes] = data[totalMinutes].split(":")
        data[totalMinutes][-1] = data[totalMinutes][-1].strip()
        data[totalMinutes][-1] = str( int(data[totalMinutes][-1] ) +1 ) 

        hours = int(data[totalMinutes][-1]) / 60
        data[totalHours] = data[totalHours].split(":")
        data[totalHours][-1] = data[totalHours][-1].strip()
        data[totalHours][-1] = str( hours  ) + "\n"

        data[totalMinutes].insert(1,":")
        data[totalMinutes] = "".join(data[totalMinutes])

        data[totalHours].insert(1,":")
        data[totalHours] = "".join(data[totalHours])

        data[totalMinutes] += "\n"

        ProductivityJournal.writeToJournal(data)

if __name__ == "__main__":
    p = ProductivityJournalUpdater("noobnoob")

    p.update()