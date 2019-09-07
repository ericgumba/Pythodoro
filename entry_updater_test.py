import unittest 

import entry_updater                    # to write to productivity-journal

class TestEntryWriter(unittest.TestCase): 
      
    def setUp(self): 
        pass
  
    # Returns True if the string contains 4 a.  /

    def testAddPomodoro(self):
        entryWriter = entry_updater.EntryUpdater("test")
        startline = 1 + 1


        beforeData = [ "all-time:1\n" "*\n\n", "test:2\n", "**\n\n"  ]

        afterData = [ "all-time:1\n" "*\n\n", "test:3\n", "***\n\n"  ]
        self.assertEqual( afterData, entryWriter.addPomodoroToTask (beforeData) )


        beforeData = [ "all-time:1\n" "*\n\n", "test:2\n", "**\n"  ]
        afterData = [ "all-time:1\n" "*\n\n", "test:3\n", "***\n"  ]
        self.assertEquals( afterData, entryWriter.addPomodoroToTask (beforeData)   )


        beforeData = [ "all-time:1\n" "*\n\n", "test:2\n", "**\n\n", "1/1/1:3" ]

        afterData = [ "all-time:1\n" "*\n\n", "test:3\n", "***\n\n"  ]
        self.assertEquals( afterData, entryWriter.addPomodoroToTask (beforeData)   )
  

if __name__ == '__main__': 
    unittest.main()