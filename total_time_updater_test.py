import unittest 

from total_time_updater import TotalTimeUpdater                   # to write to productivity-journal


TEST_JOURNAL = "test-journal"
class TestEntryWriter(unittest.TestCase): 
      
    def setUp(self): 
        pass
  
    # Returns True if the string contains 4 a.  /

    def testAddPomodoro(self): 
        beforeData = ["total-minutes-worked:57", "total-hours-worked:0"]
        afterData = ["total-minutes-worked:58", "total-hours-worked:0"] 

        self.assertEquals( afterData, TotalTimeUpdater.updateTotal(beforeData)   )
  

if __name__ == '__main__': 
    unittest.main()