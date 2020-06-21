"""
In this exercise, the task is to write a function that picks a random word
from a list of words from the SOWPODS dictionary.
Download this file and save it in the same directory as your Python code.
This file is Peter Norvig’s compilation of the dictionary of words
used in professional Scrabble tournaments.
Each line in the file contains a single word.

Hint: use the Python random library for picking a random word.

Aside: what is SOWPODS
SOWPODS is a word list commonly used in word puzzles and games (like Scrabble for example).
It is the combination of the Scrabble Player’s Dictionary and the Chamber’s Dictionary.
(The history of SOWPODS is quite interesting,
I highly recommend reading the Wikipedia article if you are curious.)

"""
from random import choice

with open('SOWPODS.txt','r') as f:
    r = f.read()

r_list = r.split('\n')
a=choice(r_list)
print(a)

'''
Another solution:

# import the random library
import random

# read all the list of words
words = []
with open('sowpods.txt', 'r') as f:
    line = f.readline().strip()
    words.append(line)
    while line:
        line = f.readline().strip()
        words.append(line)

# generate a random number
random_index = random.randint(0, len(words))

# take the word
print("Random word: ", words[random_index])
'''
