import unittest 

from entry_writer import EntryWriter                    # to write to productivity-journal


TEST_JOURNAL = "test-journal"
class TestStringMethods(unittest.TestCase): 
      
    def setUp(self): 
        pass
  
    # Returns True if the string contains 4 a. 
    def test_add_pomodoro(self):  
        EntryWriter.addPomodoroToEntry()

if __name__ == '__main__': 
    unittest.main() 