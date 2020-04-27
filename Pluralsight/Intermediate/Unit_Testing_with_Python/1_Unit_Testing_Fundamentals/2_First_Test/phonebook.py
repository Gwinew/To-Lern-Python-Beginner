"""Given a list of names and phone numbers.
    Make a Phonebook
    Determine if it is consistent:
        - no number is a prefix of another
        - e.g. Bob 91125426, Anna 97625992
        - Emergency 911
        - Bob and Emergency are inconsistent
"""

class PhoneBook:

    def __init__(self):
        self.numbers = {}
    def add(self, name, number):
#        pass
        self.numbers[name] = number
    def lookup(self, name):
        return self.numbers[name]
