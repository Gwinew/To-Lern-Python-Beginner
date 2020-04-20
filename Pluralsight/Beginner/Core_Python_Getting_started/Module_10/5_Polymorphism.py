# Polymorphism:
#
# - Using objects of different types through a uniform interface.
# - It applies to both functions as wee as more complex types.

# Polymorphism with the card printer:
# - make_boarding_card() did not rely on any concrete types.
# - Any other object that fir the interface would work in place of console_card_printer()
#
# Duck typing
#
# " When I see a bird that walks like a duck and swim like a duck and squacks like a duck, I call that bird a duck."
# - James Whitecomb Riley
#
# - An object's fitness for use is only determined at use.
# - This is in contrast to statically typed compiled languages.
# - Suitability is not determined by inherence or interfaces.
#
#
#class Aircraft:

#    def __init__(self, registration, model, num_rows, num_seats_per_row):
#        self._registration = registration
#        self._model = model
#        self._num_rows = num_rows
#        self._num_seats_per_rows = num_seats_per_row
#
#    def registration(self):
#        return self._registration
#
#    def model(self):
#        return self._model
#
#    def seating_plan(self):
#        return (range(1, self._num_rows + 1),
#                "ABCDEFGHJK"[:self._num_seats_per_rows])
#
#####################################################################

class AirbusA319:

    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def model(self):
        return "AirbusA319"

    def seating_plan(self):
        return (range(1, 23),"ABCDEF")

class Boeing777:

    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        return (range(1, 56),"ABCDEGHJK")

#####################################################################
class Flight:
    """A flight with a particulat passenger aircraft."""

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f'No airline code in "{number}"')

        if not number[:2].isupper():
            raise ValueError(f'Invalid airline code "{number}"')

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f'Invalid route number "{number}"')
        
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()                        
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.model()
        
    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def allocate_seat(self, seat, passenger):                         
        """Allocate a seat to a passenger.

        Args:
            seat: A seat designator such as '12C' or '21F'
                passenger: The passenger name.

        Raises:
            ValueError: If the seats is unavailable.
        """
        row, letter = self._parse_seat(seat)                    

        if self._seating[row][letter] is not None:
            raise ValueError(f'Seat {seat} already occupied')

        self._seating[row][letter] = passenger

    def _parse_seat(self,seat):                                 
        rows, seats_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seats_letters:
            raise ValueError(f'Invalid seat letter {letter}')

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f'Invalid row number {row}')

        if row not in rows:
            raise ValueError(f'Invalid row number {row}')

        return row, letter


    def relocate_passenger(self, from_seat, to_seat):
        """Relocate a passenger to a different seat.

        Args:
            from_seat: The existing seat designator for the
                        passanger to be moved.

            to_seat: The new seat designator.
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f'No passenger to relocate in seat {from_seat}')

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f'Seat {to_seat} already occupied')

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None


    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

    def make_boarding_cards(self, card_printer):                            
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):                                             
        """An iterable series of pasenger seating locations."""
        row_number, seat_letters = self._aircraft.seating_plan()
        for row in row_number:
            for letter in seat_letters:
                passanger = self._seating[row][letter]
                if passanger is not None:
                    yield(passanger, f'{row}{letter}')
        
def console_card_printer(passanger, seat, flight_number, aircraft):             
    output = f'| Name: {passanger}'      \
             f'  Flight: {flight_number}'\
             f'  Seat: {seat}' \
             f'  Aircraft: {aircraft} |'
    banner = '+' + '-' * (len(output) -2) + '+'
    border = '|' + ' ' * (len(output) -2) + '|'
    lines = (banner, border, output, border, banner)
    card = '\n'.join(lines)
    print(card)
    print()

def make_flights():                                         # Change the input values to two classes.         
    f = Flight("BA758", AirbusA319("G-EUPT"))

    f.allocate_seat("12A", "Guido van Rossum")
    f.allocate_seat("15F", "Bjarne Stroustrup")
    f.allocate_seat("12E", "Anders Hejlsberg")
    f.allocate_seat("1C", "John McCarthy")
    f.allocate_seat("1D", "Richard Mickey")

    g = Flight("AF758", Boeing777("F-GSPS"))

    g.allocate_seat("55K", "Guido")
    g.allocate_seat("33G", "Bjarne")
    g.allocate_seat("4B", "Anders")
    g.allocate_seat("4A", "John")
    
    return f, g

f, g = make_flights()

print(f.aircraft_model())
print(g.aircraft_model())

print(f.num_available_seats())
print(g.num_available_seats())

g.relocate_passenger("55K", "13G")
g.make_boarding_cards(console_card_printer)
