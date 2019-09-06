PRODUCTIVITY_JOURNAL = "productivity-journal"
class Journal:


    def obtainJournalData():
        with open(PRODUCTIVITY_JOURNAL, 'r') as file:  
            data = file.readlines()
        return data

    def writeToJournal(data):

        with open(PRODUCTIVITY_JOURNAL, 'w') as file:
            file.writelines( data )

    def initializeJournal(curDate):
        file_path = "productivity-journal"
        try: 
            fp = open(file_path)
        except IOError:
            fp = open(file_path,'w+')
            data = ["total-minutes-worked:0\n", "total-hours-worked:0\n\n", "all-time:0\n\n\n\n", curDate+":0\n\n\n\n"]
            fp.writelines(data)

if __name__ == "__main__":
    z = Journal()

    Journal.initializeJournal("09/05/2019")