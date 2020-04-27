"""Given a list of names and phone numbers.
    Make a Phonebook
    Determine if it is consistent:
        - no number is a prefix of another
        - e.g. Bob 91125426, Anna 97625992
        - Emergency 911
        - Bob and Emergency are inconsistent
"""

import unittest

from phonebook import PhoneBook

class PhoneBookTest(unittest.TestCase):

    def setUp(self)-> None:             # Super class
        self.phonebook = PhoneBook()

#    def tearDown(self) -> None:         # With setUp we need use tearDown - this using to release from setUp test value.
#        pass
#   Because this setUp have everything in the memory we dosen't needed this.
    
    def test_lookup_by_name(self):
#        phonebook = PhoneBook()                  
        self.phonebook.add("Bob", '12345')           # Change to self.phonebook
        number = self.phonebook.lookup("Bob")        # Change to self.phonebook
        self.assertEqual("12345", number)

    def test_missing_name(self):        
#        phonebook = PhoneBook()
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")        # Change to self.phonebook

#    @unittest.skip("WIP")                           # This features working to skip test after this command
    def test_empty_phonebook_is_consisten(self):
#        phonebook = PhoneBook()                     # We have 3 duplicates this line
        self.assertTrue(self.phonebook.is_consistent())     #  Change to self.phonebook
        
"""
class PhoneBookTest(unittest.TestCase):               # Declare a class containing test

    def setUp(self)-> None:                           # Set up fixture method
        self.phonebook = PhoneBook()

    def tearDown(self) -> None:                       # Tear down fixture method
        pass
    
    def test_lookup_by_name(self):                    # First test case
        self.phonebook.add("Bob", '12345')           
        number = self.phonebook.lookup("Bob")        
        self.assertEqual("12345", number)

    def test_missing_name(self):                      # Second test case
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")    
"""
# Test Fixture: Order of Execution

# 1. setUp()
# 2. TestCaseMethod()
# 3. tearDown()         - If everything is colapse, tearDown is end of process,
#   but if setUp() is dosen't work, then tearDown() isn't work to because it didn't take any value from setUp()


################################

# Unit test vocabulary:
#
# - Test Case
# - Test Suite
# - Test Fixture
# - Test Runner
# - Unit Under Test


#################################

# Test case:

# Delete a @unittest.skip() and add a def in PhoneBook about is_consistent().


