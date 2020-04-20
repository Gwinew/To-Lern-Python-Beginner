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
        rows, seats = self._aircraft.seating_plan()          # Create empty seating plan (empty is mean None)                           
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.model()
        
    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def allocate_seat(self, seat, passenger):                         # take allocate passanger to seat after empty seating_plan
        """Allocate a seat to a passenger.

        Args:
            seat: A seat designator such as '12C' or '21F'
                passenger: The passenger name.

        Raises:
            ValueError: If the seats is unavailable.
        """
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

        if self._seating[row][letter] is not None:
            raise ValueError(f'Seat {seat} already occupied')

        self._seating[row][letter] = passenger
        
f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows = 22, num_seats_per_row = 6))

from pprint import pprint as pp


pp(f._seating)

f.allocate_seat("12A", "Guido van Rossum")
# f.allocate_seat("12A", "Rasum Lerdorf")       # ValueError: Seat 12A already occupied
f.allocate_seat("15F", "Bjarne Stroustrup")
f.allocate_seat("12E", "Anders Hejlsberg")

# f.allocate_seat("E27", "Yukihiro Matsumoto")  # ValueError: Invalid seat letters 7
f.allocate_seat("1C", "John McCarthy")
f.allocate_seat("1D", "Richard Mickey")

# f.allocate_seat("DD", "Larry Wall")           # ValueError: Invalid seat row D

pp(f._seating)
