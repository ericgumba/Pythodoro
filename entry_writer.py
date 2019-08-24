PRODUCTIVITY_JOURNAL = "productivity-journal"

class EntryWriter:

    def addEntryToJournal( entry, startingLine ):   
        with open(PRODUCTIVITY_JOURNAL, 'r') as file: 
            data = file.readlines()
 
 
        data[startingLine] = '\n{}:1\n*\n\n'.format(entry)

        # and write everything back
        with open(PRODUCTIVITY_JOURNAL, 'w') as file:
            file.writelines( data )
 

    def addPomodoroToEntry(beginning):

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
