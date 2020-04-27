"""Given a list of names and phone numbers.
    Make a Phonebook
    Determine if it is consistent:
        - no number is a prefix of another
        - e.g. Bob 91125426, Anna 97625992
        - Emergency 911
        - Bob and Emergency are inconsistent
"""

class PhoneBook:

    def __init__(self) -> None:
        self.numbers = {}
        
    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]

def test_lookup_by_name(self):
    phonebook = PhoneBook()                  
    phonebook.add("Bob", '12345')           
    assert '1234' == phonebook.lookup("Bob")            # This is all


# To initiate test we need use to command line:
# python -m pytest
# error: AssertionError: '12345' != None



# We can add unittest to PyCharm:
# Click 'Add Configuration'
# Click '+'
# Choose Python test
# Choose pytest
# Name configuration: pytest
# Add a path to script which we want to test (or folder if script using more files)

# If test is failed then we see on the left yellow cross.

# For Working interactively: An IDE like PyCharm
# For Continues integration: A Command Line Test Runner
