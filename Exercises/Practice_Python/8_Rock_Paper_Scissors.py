"""
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them, print out
a message of congratulation to the winner, and ask
if the player want to start a new game).
"""
import random

name = input('Hello to Rock-Paper-Scissors game!\nPlease enter your name:\n')
print(f'Hi {name}!')


rps=['Rock', 'Paper', 'Scissors']


end = 'Yes'
while end == 'Yes':  
    rps_choice=random.choice(rps)
    print(rps_choice)
    enter = str(input('Please, write one of choice:\nRock\nPaper\nScissors\n\n'))
    while True:
        if (enter == 'Rock' and rps_choice == 'Scissors') or(enter == 'Scissors' and rps_choice == 'Paper') or(enter == 'Paper' and rps_choice == 'Rock'):
            print('You won!')
            break
        if enter == rps_choice:
            print('It is tie!')
            break
        else:
            print('You loose!')
            break
        if enter == 'Exit':
            break
        
    end = input('Do you want start a new game?:\nYes or No\n')

from timeit import timeit

code_1="""
enter = 'Rock'
rps_choice = 'Scissors'
if (enter == 'Rock' and rps_choice == 'Scissors') or(enter == 'Scissors' and rps_choice == 'Paper') or(enter == 'Paper' and rps_choice == 'Rock'):
    True
else:
    
    False
"""
print('code 1: ', timeit(code_1))
