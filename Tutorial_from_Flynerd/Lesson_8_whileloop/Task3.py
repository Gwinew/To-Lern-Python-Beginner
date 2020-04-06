# Expande the game from task2.py to inform user it his number is too big or too smal.
#
import random
x=random.randrange(1,30,1)
print(x)
num=int(input("Write a number\n"))
while x!=num:
    if num>x:
        print("Your number is too big")
    if num<x:
        print("Your number is too small")
    num=int(input("Try again\n"))
print("Good game!")
