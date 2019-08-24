PRODUCTIVITY_JOURNAL = "productivity-journal"

class EntryWriter:

    def addEntryToJournal( entry, startingLine ):   
        with open(PRODUCTIVITY_JOURNAL, 'r') as file: 
            data = file.readlines()
 
 
        data[startingLine] = '\n{}:1 \n \n \n'.format(entry)

        # and write everything back
        with open(PRODUCTIVITY_JOURNAL, 'w') as file:
            file.writelines( data )
 
