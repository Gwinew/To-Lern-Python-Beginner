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

    def test_lookup_by_name(self):
        phonebook = PhoneBook()                  
        phonebook.add("Bob", '12345')           
        number = phonebook.lookup("Bob")        
        self.assertEqual("12345", number)



    def test_missing_name(self):        # What happend if we have name which doesn;t exist in phonebook
        phonebook = PhoneBook()
        with self.assertRaises(KeyError):
            phonebook.lookup("missing")


# Test is pass because we use the dictionary in Phonebook.
#
# Unit test Vocabulary: Test Suite
