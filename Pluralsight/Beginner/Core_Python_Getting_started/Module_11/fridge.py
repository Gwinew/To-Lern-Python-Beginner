"""Demonstrate raiding a refrigerator"""

from contextlib import closing                      # 2 - add import

class RefrigeratorRaider:                           # A class for raiding the fridge
    """Raid a refrigerator"""

    def open(self):                                 # Open the refrigerator door
        print("open fridge door.")

    def take(self, food):                           # Take some food
        print(f'Finding {food}...')
        if food == 'deep fried pizza':
            raise RuntimeError('Health warning!')
        print(f'Taking {food}')

    def close(self):                                # Close the refigerator door
        print('Close fridge door')

def raid(food):                                     # Raid for some food!
    with closing(RefrigeratorRaider()) as r:
#    r = RefrigeratorRaider()                       # 2 - change to with-block
        r.open()
        r.take(food)
#        r.close()                                  # 3 - removed explicit call to close()
