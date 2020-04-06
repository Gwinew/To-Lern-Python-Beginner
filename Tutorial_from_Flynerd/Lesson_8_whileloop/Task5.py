# Using random module create a another simple game. Computer a draw lot word from list range.
# Next the letters are lotterying and show this to guess for user.
# User guesses until he or she find out correct answer and game is over.
#
# Press "q" or "Q" to end a game.
import random
names=("andrzej","krzysztof", "andzelika", "ewelina")
num=len(names)
name=names[random.randrange(0,num,1)]
numname=len(name)
namesample=random.sample(name,numname)
yourname=input("Write a name from this letters: {}\n".format(namesample))
while name != yourname:
    if yourname == "q" or yourname == "Q":
        break
    yourname=input("Try again: {}\n".format(namesample))
print("Game is over!")
