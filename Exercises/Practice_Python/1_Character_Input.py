""" Create a program that asks the user to enter their name and their age.
    Print out a message addressed to them that tells them the year that they will turn 100 years old.

    Extras:
    1. Add on the previous program by asking the user for another number and printing out that many copies of the precious message.
    2. Print out that many copes of the previous message on separate lines.
"""

name=input('Hi! What\'s your name?\n')
age=input(f'Hi {name}!\nPlease, write your age:\n')

print(f'You left {100-int(age)} years to will turn 100 years old!')

number = input('Please, give a number 1-20:\n')

x = range(int(number))

for i in x:
    print(f'You left {100-int(age)} years to will turn 100 years old!\n')
