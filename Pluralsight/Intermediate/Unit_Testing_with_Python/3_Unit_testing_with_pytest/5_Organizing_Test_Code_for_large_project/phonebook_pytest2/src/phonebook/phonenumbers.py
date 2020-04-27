"""Given a list of names and phone numbers.
    Make a Phonebook
    Determine if it is consistent:
        - no number is a prefix of another
        - e.g. Bob 91125426, Anna 97625992
        - Emergency 911
        - Bob and Emergency are inconsistent
"""
import os

from phonebook.data_processing import clean_phonenumber

class PhoneBook:

    def __init__(self, cache_directory=None):
        self.numbers = {}
        cache_dir = cache_directory or os.getcwd()
        self.filename = os.path.join(cache_dir, 'phonebook.txt')
        self.cache = open(self.filename, 'w')
        
    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return set(self.numbers[name])

    def is_consistent(self):
        for name1, number1 in self_numbers.item():
            for name2, number2 in self.numbers.items():
                if name1 == name2:
...
    def clear(self):
        self.chache.close()
        os.remove(self.filename)
