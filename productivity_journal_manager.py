
class ProductivityJournalManager:
    def __init__(self, productivityJournalUpdater): 
        self.productivityJournalUpdater = productivityJournalUpdater


    def updateProductivityJournal(self):
        self.productivityJournalUpdater.update()
    