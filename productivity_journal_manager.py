
from productivity_journal_updater import ProductivityJournalUpdater

class ProductivityJournalManager:
    def __init__(self, task = None): 
        self.task = task

        if self.task:
            self.productivityJournalUpdater = ProductivityJournalUpdater(task)
        else:
            self.productivityJournalUpdater = ProductivityJournalUpdater()


    def updateProductivityJournal(self):
        self.productivityJournalUpdater.update()
    


# class JournalWriter:
#     def __init__(self, task:str = None): 
#         self.task = task
#         Journal.initializeJournal(date.getCurrentDate())
#         if self.task:
#             self.entryUpdater = entry_updater.EntryUpdater (task)
#         else:
#             self.entryUpdater = entry_updater.EntryUpdater(task)