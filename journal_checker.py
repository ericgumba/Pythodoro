PRODUCTIVITY_JOURNAL = "productivity-journal"
# CHECKS TO SEE IF ENTRY OR TASK IS IN JOURNAL.


class JournalChecker: 

    def inJournal(Entry): 

        with open(PRODUCTIVITY_JOURNAL) as myFile:
 
            for line in myFile:
                if line[0].isdigit() or line[0] == 'a':
                    if Entry in line:
                        return True
            return False
            


    
    def getBeginningAndEndOfEntry(time):   

        with open(PRODUCTIVITY_JOURNAL) as myFile:
            lastLineNumberRead = 0
            beginning = 0
            for num, line in enumerate(myFile, 1):
                if time in line: 
                    beginning = num
                elif line[0].isdigit():
                    end = num
                    lastLineNumberRead = num
                    break


                lastLineNumberRead = num

            
            assert beginning > 0, "Beginning of entry should be greater than 0"
            assert end <= lastLineNumberRead, "End of entry is greater than the number of lines in the file"


            return  ( beginning, end ) 