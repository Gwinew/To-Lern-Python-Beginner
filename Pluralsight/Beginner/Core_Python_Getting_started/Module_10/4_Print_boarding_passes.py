# Print Boarding Card.
#
# - Print boarding cards in alphabetical order.
# - Separation of concern: don't put this on the Flight class
# - Remember that functions are objects, too!
#
# Tell! Don't ask.
#
# - Tell other objects what to do instead of asking them their state and responding to it.

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
        row, letter = self._parse_seat(seat)                    # Copy sequence and create reference 

        if self._seating[row][letter] is not None:
            raise ValueError(f'Seat {seat} already occupied')

        self._seating[row][letter] = passenger
####################################################################
    def _parse_seat(self,seat):                                 # paste sequence and create a rule
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
####################################################################

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

    def make_boarding_cards(self, card_printer):                            # Make a sort alphabetical with pasanger from the generator
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):                                             # Make a value to separate a pasanger from all list - create a generator
        """An iterable series of pasenger seating locations."""
        row_number, seat_letters = self._aircraft.seating_plan()
        for row in row_number:
            for letter in seat_letters:
                passanger = self._seating[row][letter]
                if passanger is not None:
                    yield(passanger, f'{row}{letter}')
        
def console_card_printer(passanger, seat, flight_number, aircraft):             # Make a operation to print a passanger card
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

def make_flight():                                                  
    f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows = 22, num_seats_per_row = 6))

    f.allocate_seat("12A", "Guido van Rossum")
    f.allocate_seat("15F", "Bjarne Stroustrup")
    f.allocate_seat("12E", "Anders Hejlsberg")
    f.allocate_seat("1C", "John McCarthy")
    f.allocate_seat("1D", "Richard Mickey")
    return f

f = make_flight()

f.relocate_passenger("12A", "15D")

print(f.make_boarding_cards(console_card_printer))
