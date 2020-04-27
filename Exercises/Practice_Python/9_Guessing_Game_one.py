"""Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right.
(Hint: remember to use the user input lesson from the very firs exercise).

    Extras:

    1. Keep the game going until the user types 'exit'
    2. Keep track of how many guesses the user has taken,
        and when the game ends, print this out.
"""

import random

number = random.randint(1,9)
print(number)
x = 0
user_number=input('Guess a number:\n')

if user_number == 'exit':
    print('Game over!')
else:
    x = 1
    while int(user_number) != number:
        if int(user_number) < number:
            print('Too low')
        if int(user_number) > number:
            print('Too high')
        user_number = input('Try again! Guess the number!\n')
        x += 1
        if user_number == 'exit':
            break
    print(f'This is correct number. You have guess {x} times')
