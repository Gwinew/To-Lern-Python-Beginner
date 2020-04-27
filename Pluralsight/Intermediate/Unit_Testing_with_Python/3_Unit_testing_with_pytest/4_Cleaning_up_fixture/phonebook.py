"""Given a list of names and phone numbers.
    Make a Phonebook
    Determine if it is consistent:
        - no number is a prefix of another
        - e.g. Bob 91125426, Anna 97625992
        - Emergency 911
        - Bob and Emergency are inconsistent
"""

class PhoneBook:

    def __init__(self, cache_directory):
        self.numbers = {}
        self.filename = os.path.join(cache_directory, 'phonebook.txt')
        self.cache = open(self.filename, 'w')
        
    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return set(self.numbers[name])

    def clear(self):
        self.chache.close()
        os.remove(self.filename)
