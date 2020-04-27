# Better test

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
    
    def test_lookup_by_name(self):              
                  
        self.phonebook.add("Bob", '12345')      
        number = self.phonebook.lookup("Bob")   
        self.assertEqual("12345", number)       

    def test_missing_name(self):        

        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")        
                         
    def test_empty_phonebook_is_consisten(self):
        self.assertTrue(self.phonebook.is_consistent())    

#######################
# Retribution test_is_consistent

    def test_is_consistent_with_different_enteries(self):   #change a name                               
        self.phonebook.add("Bob", '12345')                      
        self.phonebook.add("Anna", '012345')                    
        self.assertTrue(self.phonebook.is_consistent())
        
    def test_inconsistent_with_duplicate_enteries(self):
        self.phonebook.add("Bob", '12345')
        self.phonebook.add("Sue", '12345')  
        self.assertFalse(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_prefix(self):
        self.phonebook.add("Bob", '12345')
        self.phonebook.add("Sue", '123')    
        self.assertFalse(self.phonebook.is_consistent())        
        
# Change in phonebook.py - add for name1, etc.


