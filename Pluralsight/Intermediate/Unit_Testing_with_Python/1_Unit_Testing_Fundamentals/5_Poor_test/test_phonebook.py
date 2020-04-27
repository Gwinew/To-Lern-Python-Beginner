# Poor test case

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

    def setUp(self)-> None:            
        self.phonebook = PhoneBook()
    
    def test_lookup_by_name(self):              # Test Case name
                  
        self.phonebook.add("Bob", '12345')      # Arrange
        number = self.phonebook.lookup("Bob")   # Act
        self.assertEqual("12345", number)       # Assert

    def test_missing_name(self):        

        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")        

                         
    def test_empty_phonebook_is_consisten(self):
        self.assertTrue(self.phonebook.is_consistent())    

    def test_is_consistent(self):                               # Test Case Name
        self.phonebook.add("Bob", '12345')                      # Act
        self.assertTrue(self.phonebook.is_consistent())         # Assert
        self.phonebook.add("Anna", '012345')                    # Act
        self.assertTrue(self.phonebook.is_consistent())         # Assert
        self.phonebook.add("Sue", '12345')  # identical to Bob  # Act
        self.assertFalse(self.phonebook.is_consistent())        # Assert
        self.phonebook.add("Sue", '123')    # prefix of Bob     # Act
        self.assertFalse(self.phonebook.is_consistent())        # Assert
        
# This list of tests is very poor.
# Many little tests is doing on one frame of test.
# The better idea is creating different test for situation:

# - Lookup by name
# - Missing name
# - Consistent when empty
# - Consistent when all different
# - Inconsistent when duplicates
# - Inconsistent when duplicates prefix

# The Three Parts of a Test:

# - Arrange: Set up the object to be tested, and collaborators.
# - Act: Exercise the unit under test
# - Assert: Make claims aboit what happend


