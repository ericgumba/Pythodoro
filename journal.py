PRODUCTIVITY_JOURNAL = "productivity-journal"
class Journal:


    def obtainJournalData():
        with open(PRODUCTIVITY_JOURNAL, 'r') as file:  
            data = file.readlines()
        return data

    def writeToJournal(data):

        with open(PRODUCTIVITY_JOURNAL, 'w') as file:
            file.writelines( data )