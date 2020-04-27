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
        return set(self.numbers[name])

@pytest.fixture
def phonebook():
#    phonebook = Phonebook()
    return Phonebook()          # instead phonebook

def test_lookup_by_name(phonebook):
#    phonebook = PhoneBook()           # Create a method from this line       
    phonebook.add("Bob", '1234')           
    assert '1234' == phonebook.lookup("Bob")

def test_phonebook_contains_all_names(phonebook):
#    phonebook = PhoneBook()                  
    phonebook.add("Bob", '1234')           
#    assert phonebook.names() == {"Bob", "Missing"}
    assert "Bob" in phonebook.names()

def test_missing_name_raises_error(phonebook):
#    phonebook = Phonebook()             
#    phonebook.add("Bob", "1234")
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")
