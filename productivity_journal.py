PRODUCTIVITY_JOURNAL = "productivity-journal"

class ProductivityJournal:


    def obtainJournalData():
        with open(PRODUCTIVITY_JOURNAL, 'r') as file:  
            data = file.readlines()
        return data

    def writeToJournal(data):

        with open(PRODUCTIVITY_JOURNAL, 'w') as file:
            file.writelines( data )

    def initializeJournal(curDate):
        file_path_1 = PRODUCTIVITY_JOURNAL 
        try: 
            fp = open(file_path_1)
        except IOError:
            fp = open(file_path_1,'w+')
            data = ["all-time\n","total-minutes-worked:0\n", "total-hours-worked:0\n\n\n", curDate+"\n"+ "total-minutes-worked:0\n" + "total-hours-worked:0" + "\n\n\n\n"]
            fp.writelines(data)

if __name__ == "__main__":
    z = ProductivityJournal()

    ProductivityJournal.initializeJournal("09/05/2019")