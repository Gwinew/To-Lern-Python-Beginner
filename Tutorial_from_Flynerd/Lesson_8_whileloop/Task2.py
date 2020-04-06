# Get to know the random module
# import random
#
# Create a simple game for quiz. Computer draws value from 1 to 30.
# Ask a user to try to guess a number. Computer asking user until user is put cottect answer.
import random
x=random.randrange(1,30,1)
number=int(input("Guess a number\n"))
while x!=number:
    number=int(input("Try again\n"))
print("You are did it!")
