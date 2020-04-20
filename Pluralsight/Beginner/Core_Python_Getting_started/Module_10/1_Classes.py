# Types and Classes.
#
#
# Classes:
#
# - Define the structure and behavior of objects.
# - Act as a template for creating new objects.
# - Classes control an object's initial state, attributes and methods
#
#
# Object-oriented programing:
#
# - Classes can make complex problem tractable.
# - But they can make simpe problems unnecessarily complex.
# - Python lets you strike the right balance between fynctions and classes.
#
# ############
# Defining Classes:
#
# class MyClassName: <- By convention, class names use CamelCase

"""Model for aircraft flights."""

class Flight:
    pass

# If in console use: from airtravel import Flight <-airtravel is name of file when is class Flight...
# And use "Flight" then we have <class 'airtravel.Flight'>

print(Flight) # When we use in inside a file then we have <class '__main__.Flight'>

f = Flight()

print(f)        # f is a class now and we have <__main__.Flight object at ...>

# More intresting with class

class Flight:
    def number(self):
        return "SN060"
f= Flight()

print(f.number())           # SN060
print(Flight.number(f))     # SN060
##################################

#
# __init__()
#
# - Instance method for initializing new objects.
# - Is an initializer, not a constructor.
# 

class Flight:

    def __init__(self, number):         # 'self' is similar to 'this' in Java, C# or C++
        self._number = number           # Why _number? Avoid name clash with number() - By convention, implementation details start with underscore

    def number(self):
        return self._number

f = Flight('SN060')
print(f.number())           # SN060
print(f.number)             # <bound method Flight.number of <__main__.Flight object at 0x0000000002F7BA90>>
#
# Good practis is Class Invariants
# - Truths about an object that endure for its lifetime.

class Flight:

    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError(f'No airline code in "{number}"')

        if not number[:2].isupper():
            raise ValueError(f'Invalid airline code "{number}"')

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f'Invalid route number "{number}"')
        
        self._number = number
        
    def number(self):
        return self._number

f = Flight("SN060")
# f = Flight("060")         # ValueError: No airline code in "060"
# f = Flight("sn060")       # ValueError: Invalid airline code "sn060"
# f = Flight("snabc")       # ValueError: Invalid airline code "snabc"
# f = Flight("SN12345")     # ValueError: Invalid route number "SN12345"
#
class Flight:

    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError(f'No airline code in "{number}"')

        if not number[:2].isupper():
            raise ValueError(f'Invalid airline code "{number}"')

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f'Invalid route number "{number}"')
        
        self._number = number
        
    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

###############

class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_rows = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seats_per_rows])

a = Aircraft("G-EUPT", "Airbus A319", num_rows = 22, num_seats_per_row = 6)
print(a.registration())
print(a.model())
print(a.seating_plan())
################################
# The Law of Demetr:
# - The principle of least knowledge.
# - Only talk to your friends.


class Flight:
    """A flight with a particulat pasenger aircraft."""

    def __init__(self, number, aircraft):                           # Add aircraft
        if not number[:2].isalpha():
            raise ValueError(f'No airline code in "{number}"')

        if not number[:2].isupper():
            raise ValueError(f'Invalid airline code "{number}"')

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f'Invalid route number "{number}"')
        
        self._number = number
        self._aircraft = aircraft

    def aircraft_model(self):                                       # from aircraft value witch ( aircraft = Aircraft(registration = "G-EUPT", model = "Airbus A319", num_rows = 22, num_seats_per_row = 6)) find a .model()
        return self._aircraft.model()
        
    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]
f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows = 22, num_seats_per_row = 6))
print(f.aircraft_model())
