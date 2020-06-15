'''
In a Previous exercise we've written a program that 'knows' a number
and ask a user to guess it.

This time, we're going to do exactly the opposite. You, the user,
will have in your head a number between 0 and 100. The program will guess a number,
and you, the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses
it took to get your number.

As the writer of this program, you will have to choose how your program
will stategically guess. A naive strategy can be to simply start the guessing at 1,
and keep going (2,3,4 etc) until you hit the number. But that's not
an optimal guessing strategy. An alternate strategy might be to guess 50
(right in the middle of the range), and then icrease/decrease by 1 as needed.
After you've written the program, try to find the optimal strategy!
(We'll talk about what is the optimal one next week with the solution.)
'''
from random import randrange
print('This is a play in Guessing number, but I will try to guess.\n'
        ' Choose number from 0 to 100.')

x_1=0
x_2=101

x = randrange(x_1,x_2)

counter =0
while True:
    temp = x
    counter += 1
    num = input(f'{x} - This is your number?\nPlese, choose:\n'
    '"H" - Too High\n'
    '"L" - Too Low\n'
    '"Y" - Yes this is that number\nYour answer: ')
    if num == "H":
        x_2 = temp
    if num == "L":
        x_1 = temp + 1
    if x_2 - x_1 == 1:
        print(f'Your number is {x_1}')
        break
    if num == "Y":
        break
    x = randrange(x_1,x_2)
print(f'End game after {counter} shots')
