 # CHECKS TO SEE IF ENTRY OR TASK IS IN JOURNAL. 
from productivity_journal import ProductivityJournal
class ProductivityJournalChecker: 
    def inJournal(Entry):  
        data = ProductivityJournal.obtainJournalData() 
 
        for line in data:
            if line[0].isdigit() or line[0] == 'a':
                if Entry in line:
                    return True
        return False
             

    def taskInEntry(entry, data, task, beginningAndEndOfEntry): 
        
 
        for i in range(beginningAndEndOfEntry[0], beginningAndEndOfEntry[1]): 
            if task in data[i]:
                return True
        
        return False


    def getBeginningAndEndOfEntry(time):   

        data = ProductivityJournal.obtainJournalData()

        lastLineNumberRead = 0
        beginning = 0
        for num, line in enumerate(data):
            if time in line: 
                beginning = num
            elif line[0].isdigit():
                end = num
                lastLineNumberRead = num
                break
            lastLineNumberRead = num

        end = lastLineNumberRead  

        return  ( beginning, end )