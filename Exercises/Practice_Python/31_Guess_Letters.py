"""
Let’s continue building Hangman. In the game of Hangman,
a clue word is given by the program that the player has to guess, letter by letter.
The player guesses one letter at a time until the entire word has been guessed.
(In the actual game, the player can only guess 6 letters incorrectly before losing).

Let’s say the word the player has to guess is “EVAPORATE”.
For this exercise, write the logic that asks
a player to guess a letter and displays letters in the clue word
that were guessed correctly. For now, let the player guess
an infinite number of times until they get the entire word. As a bonus,
keep track of the letters the player guessed and display a different message if
the player tries to guess that letter again.
Remember to stop the game when all the letters have been guessed correctly!
Don’t worry about choosing a word randomly or keeping track of the number
of guesses the player has remaining - we will deal with those in a future exercise.

An example interaction can look like this:

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...
And so on, until the player gets the word.
"""



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
    letter.upper().strip()
    return letter

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


print('Welcome to Hangman!')
e = 'Y'
while e == 'Y':
    game_word = "EVAPORATE"
    stw = start_game_word(game_word)
    a = True
    while a == True:
        print(show_stw(stw))
        letter = input('Guess your letter: ')
        if letter == 'exit' or letter == 'EXIT' or letter == 'Exit':
            break
        letter = inp_lett(letter)
        if len(letter) == 1:
            c = finding_letter(game_word, letter)
            if c == []:
                print('Incorect!')
            else:
                stw = changing_letter(game_word, stw, letter, c)
                en = ending(stw)
                if en == 0:
                    print('This is End!')
                    e = input('Do You want play again?\n"Y" for Yes\n"N" for No:\n')
                    a = False
        else:
            print('Incorect number of letters. Please guess again...')
