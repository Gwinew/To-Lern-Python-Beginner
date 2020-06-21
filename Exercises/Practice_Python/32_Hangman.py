"""
In this exercise, we will finish building Hangman.
In the game of Hangman, the player only has
6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.

In Part 1, we loaded a random word list and picked a word from it.
In Part 2, we wrote the logic for guessing the letter
and displaying that information to the user.
In this exercise, we have to put it all together and add logic for handling guesses.

Copy your code from Parts 1 and 2 into a new file as a starting point.
Now add the following features:

Only let the user guess 6 times, and tell the user how many guesses they have left.
Keep track of the letters the user guessed.
If the user guesses a letter they already guessed,
don’t penalize them - let them guess again.
Optional additions:

When the player wins or loses, let them start a new game.
Rather than telling the user "You have 4 incorrect guesses left",
display some picture art for the Hangman.
This is challenging - do the other parts of the exercise first!
Your solution will be a lot cleaner if you make use of functions to help you!
"""
from random import choice


def pick_word():
    with open('SOWPODS.txt','r') as f:
        r = f.read()
    r_list = r.split('\n')
    word = choice(r_list)
    return word


def start_game_word(game_word):
    count_letter = len(game_word) - 1
    stw = "_" + "_" * count_letter
    return stw

def finding_letter(game_word, input_letter):
    list_letter = []
    next = 0
    a = True
    while a == True:
        b = game_word.find(input_letter, next)
        if b == -1:
            break
        else:
            list_letter.append(b)
            c = len(game_word)
            if b != (c - 1):
                next = b + 1
            else:
                break
    return list_letter

def inp_lett(letter):
    return letter.upper().strip()

def changing_letter(game_word, stw, letter, list_letter):

    while True:
        if list_letter == []:
            break
        else:
            num = list_letter[0]
            list_stw = list(stw)
            list_stw[num] = letter
            stw = "".join(list_stw)
            del list_letter[0]
    return stw

def show_stw(stw):
    stw = " ".join(stw)
    return stw

def ending(stw):
    return stw.count('_')


def show_picture(count_lose):
    if count_lose == 0:
        a = "     ____   \n\
    |    |  \n\
    |       \n\
    |       \n\
    |       \n\
   _|_\n"
        return a
    if count_lose == 1:
        a = "     ____   \n\
    |    |  \n\
    |    O  \n\
    |       \n\
    |       \n\
   _|_\n"
        return a
    if count_lose == 2:
        a = "     ____   \n\
    |    |  \n\
    |    O  \n\
    |    |  \n\
    |       \n\
   _|_\n"
        return a
    if count_lose == 3:
        a = "     ____   \n\
    |    |  \n\
    |    O  \n\
    |    |\\ \n\
    |       \n\
   _|_\n"
        return a
    if count_lose == 4:
        a = "     ____   \n\
    |    |  \n\
    |    O  \n\
    |   /|\\ \n\
    |       \n\
   _|_\n"
        return a
    if count_lose == 5:
        a = "     ____   \n\
    |    |  \n\
    |    O  \n\
    |   /|\\ \n\
    |     \\ \n\
   _|_\n"
        return a
    if count_lose == 6:
        a = "     ____   \n\
    |    |  \n\
    |    O  \n\
    |   /|\\ \n\
    |   / \\ \n\
   _|_\n"
        return a

def lib_correct_letter(letter, lib_c_l):
    if letter in lib_c_l:
        return 0
    else:
        lib_c_l.add(letter)

def lib_incorrect_letter(letter, lib_i_l):
    if letter in lib_i_l:
        return 0
    else:
        lib_i_l.add(letter)

lib_i_l = set()
lib_c_l = set()
print('Welcome to Hangman!')
e = 'Y'
while e == 'Y':
    game_word = pick_word()
    stw = start_game_word(game_word)
    count_lose = 0
    while count_lose != 6:
        if count_lose == 2:
            print("You have 4 shoots.")
        print(show_picture(count_lose))
        print(show_stw(stw))
        letter = input('Guess your letter: ')
        if letter == 'exit' or letter == 'EXIT' or letter == 'Exit':
            break
        letter = inp_lett(letter)
        if len(letter) == 1:
            c = finding_letter(game_word, letter)
            if c == []:
                if letter in lib_i_l:
                    print("Come on... You already wrote this letter...")
                else:
                    lib_i_l.add(letter)
                    print('Incorect!')
                    count_lose += 1
                    if count_lose == 6:
                        print(show_picture(count_lose))
                        print(game_word)
            else:
                if letter in lib_c_l:
                    print("Come on... You already wrote this letter...")
                else:
                    lib_c_l.add(letter)
                    stw = changing_letter(game_word, stw, letter, c)
                    en = ending(stw)
                    if en == 0:
                        print('You win! Congratulation!')
                        break
        else:
            print('Incorect number of letters. Please guess again...')
    e = input('Do You want play again?\n"Y" for Yes\n"N" for No:\n')
    e = inp_lett(e)
print("End")
