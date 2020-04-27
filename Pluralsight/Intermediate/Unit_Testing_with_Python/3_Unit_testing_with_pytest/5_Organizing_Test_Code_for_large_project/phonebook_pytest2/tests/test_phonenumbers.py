"""Given a list of names and phone numbers.
    Make a Phonebook
    Determine if it is consistent:
        - no number is a prefix of another
        - e.g. Bob 91125426, Anna 97625992
        - Emergency 911
        - Bob and Emergency are inconsistent
"""
"""
class PhoneBook:

    def __init__(self) -> None:
        self.numbers = {}
        
    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return set(self.numbers[name])

    def clear(self):
        pass

Move this to phonebook.py
"""
"""
@pytest.fixture
def phonebook():
    return Phonebook()

Modify
"""
@pytest.fixture
def phonebook(tmpdir):
    "Provides an empty Phonebook"
#    phonebook = Phonebook(tmdir)
    return Phonebook(tmdir)
#    yield phonebook
#    phonebook.clear()
    
def test_lookup_by_name(phonebook):
    phonebook.add("Bob", '1234')           
    assert '1234' == phonebook.lookup("Bob")

def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Bob", '1234')           
    assert "Bob" in phonebook.names()

def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")



# If you want to look at fixtures in pytest:
# in command line:
# pytest --fixtures
