"""Given a list of names and phone numbers.
    Make a Phonebook
    Determine if it is consistent:
        - no number is a prefix of another
        - e.g. Bob 91125426, Anna 97625992
        - Emergency 911
        - Bob and Emergency are inconsistent
"""

import unittest

#class PhoneBook:               # Right-click, choose Refactor, and choose Move... to phonebook.py
#    pass
from phonebook import PhoneBook

class PhoneBookTest(unittest.TestCase):

    def test_lookup_by_name(self):
        phonebook = PhoneBook()                 # Click alt+enter and choose a create new class 
        phonebook.add("Bob", '12345')           # PyCharm is highlight a word which needed to define -> click right ande choose 'Add method add() to class PhoneBook'
        number = phonebook.lookup("Bob")        # Click 'Add method lookup() to class PhoneBook'
        self.assertEqual("12345", number)


# To initiate test we need use to command line:
# python -m unittest
# error: AssertionError: '12345' != None



# We can add unittest to PyCharm:
# Click 'Add Configuration'
# Click '+'
# Choose Python test
# Choose Unittest
# Name configuration: Unittest
# Add a path to script which we want to test (or folder if script using more files)

# If test is failed then we see on the left yellow cross.

# For Working interactively: An IDE like PyCharm
# For Continues integration: A Command Line Test Runner
