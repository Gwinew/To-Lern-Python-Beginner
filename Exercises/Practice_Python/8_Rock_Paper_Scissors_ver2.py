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

end = ['Yes', 'No']
end_int = 1
while end_int == 1:
    x=0
    y=0
    while x <= 2 and y <= 2:
        rps_choice=random.choice(rps)
        print(rps_choice)
        enter_int = int(input('Please, write number from one of choice:\n1. Rock\n2. Paper\n3. Scissors\n\n')) -1
        enter=rps[enter_int]
        print(enter)
        
        if (enter == 'Rock' and rps_choice == 'Scissors') or(enter == 'Scissors' and rps_choice == 'Paper') or(enter == 'Paper' and rps_choice == 'Rock'):
            x+=1
            print('You won!')
        elif enter == rps_choice:
            print('It is Tie')
        else:
            print('You loose!')
            y += 1
            
        if enter == 'Exit':
            break
        print(x,y)
    if x > y:
        print(f'{name}! You won the battle!')
    else:
        print('You loose the battle...')
    end_int = int(input('Do you want start a new game?:\n1. Yes or 2. No\n'))




