 # CHECKS TO SEE IF ENTRY OR TASK IS IN JOURNAL.
from journal import Journal
import string


def removeAllWhiteSpaces(word):
    return word.translate({ord(c): None for c in string.whitespace})

class JournalChecker: 

    def inJournal(Entry):  

        data = Journal.obtainJournalData()
 
        for line in data:
            if line[0].isdigit() or line[0] == 'a':

                if Entry in line:
                    return True
        return False
             

    def taskInEntry(entry, data, task, beginningAndEndOfEntry): 
        
 
        for i in range(beginningAndEndOfEntry[0], beginningAndEndOfEntry[1]): 
            line = removeAllWhiteSpaces(data[i])
            journalTask = line.split(":")[0]
            if task == journalTask:
                return True
        
        return False


    def getBeginningAndEndOfEntry(time):   # entry AKA 'time' will always be in journal
        data = Journal.obtainJournalData()
 

        lastLineNumberRead = 0
        beginning = 0
        for num, line in enumerate(data):

            if line[0].isdigit() or line[0] == 'a': # so a task isn't accidentally mistaken as an entry

                if time in line: 
                    beginning = num
                elif line[0].isdigit():
                    end = num
                    lastLineNumberRead = num
                    break
            lastLineNumberRead = num

        end = lastLineNumberRead
        assert beginning > 0, "Beginning of entry should be greater than 0"
        assert end <= lastLineNumberRead, "End of entry is greater than the number of lines in the file"


        return  ( beginning, end ) 


if __name__ == "__main__":
    a =JournalChecker.taskInEntry('all-time', Journal.obtainJournalData(), 'jo', JournalChecker.getBeginningAndEndOfEntry('all-time') )

    print( a )