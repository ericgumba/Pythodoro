from .productivity_journal import ProductivityJournal
import string
def removeAllWhiteSpaces(word):
    return word.translate({ord(c): None for c in string.whitespace})

class ProductivityJournalChecker: 
    def inJournal(Entry):   # Entry is either all-time or current date
        data = ProductivityJournal.obtainJournalData() 
 
        for line in data:
            
            if line[0].isdigit() or line[0] == 'a':
                if Entry == removeAllWhiteSpaces(line):
                    return True
        return False
             

    def taskInEntry(entry, data, task, beginningAndEndOfEntry): 
        
 
        for i in range(beginningAndEndOfEntry[0], beginningAndEndOfEntry[1]): 
            if task == removeAllWhiteSpaces (data[i]) :
                return True
        
        return False

    def getIndexOfTask(begin, end, task): # task will always be in entry

        data = ProductivityJournal.obtainJournalData() 
        for i in range(begin, end):
            
            if task == removeAllWhiteSpaces( data[i] ):
                return i

    def getBeginningAndEndOfEntry(time):   

        data = ProductivityJournal.obtainJournalData()

        lastLineNumberRead = 0
        beginning = 0
        for num, line in enumerate(data):
            if time == removeAllWhiteSpaces (line): 
                beginning = num
            elif line[0].isdigit():
                end = num
                lastLineNumberRead = num
                break
            lastLineNumberRead = num

        end = lastLineNumberRead  

        return  ( beginning, end )

if __name__ == "__main__":  

    ala = "asdsfa\n \t as d gfe ihetw sad"

    print(removeAllWhiteSpaces(ala))

    print(ProductivityJournalChecker.inJournal("all-time"))

    print(ProductivityJournalChecker.inJournal('9/13/2019'))
    print(ProductivityJournalChecker.inJournal('9/11/2019')) 
    data = ProductivityJournal.obtainJournalData() 

    print(ProductivityJournalChecker.taskInEntry('all-time', data, "j",  ProductivityJournalChecker.getBeginningAndEndOfEntry('all-time') ) == False)

    #fix get indexOfTask
    # convert data[i] into a string without whitespaces
    # return true if task == data[i]

    #fix getbeginningandendofentry
    # why? because of "if time in line"  