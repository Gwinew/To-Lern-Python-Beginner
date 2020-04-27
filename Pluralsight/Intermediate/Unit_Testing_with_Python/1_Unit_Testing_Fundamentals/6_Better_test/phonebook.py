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
        self.numbers[name] = number
    def lookup(self, name):
        return self.numbers[name]

    def is_consisten(self):
        for name1, number1 in self.numbers.items():        # brute-force implementation
            for name2, number2 in self.numbers.items():     # double loop in brute-force
                if name1==name2:
                    continue
                if number1.startswith(number2):
                    return False
        return True

# git hub repository to looking to something:

# https://github.com/emilybache/Phone-Numbers-Kata
