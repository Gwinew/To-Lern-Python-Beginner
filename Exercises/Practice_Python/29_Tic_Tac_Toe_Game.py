"""
In 3 prevoius exercises, we build up a few components needed to build a Tic Tac
Toe Game in Python.

The next step is to put all these three components together to make
a two-player Tic Tac Toe game!
Your challenge in this exercise is to use the functions
from those previous exercises all together in the same program
to make a two-player game that you can play with a friend.
There are a lot of choices you will have to make when completing this exercises,
so you can go as fat as little as you want with it.

Here are a few things to keep in mind:
- You should keep track of who won - if there is a winner,
show a congratulatory message on the screen.

- If there are no more moves left, don't ask for the next player's move!

As a bonus, you can ask the player if they want to play again and keep
a running tally of who won more - Player 1 or Player 2.
"""
def board_game(nmt):
    return f' --- --- --- \n| {nmt[0][0]} | {nmt[0][1]} | {nmt[0][2]} |\n --- --- --- \n| {nmt[1][0]} | {nmt[1][1]} | {nmt[1][2]} |\n --- --- --- \n| {nmt[2][0]} | {nmt[2][1]} | {nmt[2][2]} |\n --- --- --- '

def check_grid(nmt):
    #row
    for i in range(3):
        num = set(nmt[i])
        if len(num)==1 and nmt[i][0] != 0:
            return nmt[i][0]

    #column
    for i in range(3):
        num = set([nmt[0][i],nmt[1][i],nmt[2][i]])
        if len(num)==1 and nmt[0][i] !=0:
            return nmt[0][i]

    #diagonal
    num = set([nmt[0][0],nmt[1][1],nmt[2][2]])
    if len(num)==1 and nmt[0][0] !=0:
        return nmt[0][0]
    num = set([nmt[0][2],nmt[1][1],nmt[2][0]])
    if len(num)==1 and nmt[0][2] !=0:
        return nmt[0][2]
    return 0

def turn_value(sentence):
    value = input(sentence +'\nPlease enter a value as example "row,column" to put your move:\n')
    value_list = value.split(',')
    num1 = int(value_list[0])-1
    num2 = int(value_list[1])-1
    return num1, num2


def input_player_value(countx, counto, nmt, sen_x, sen_o, sen_again):
    if countx <= counto:
        x = turn_value(sen_x)
        countx+=1
        n1 = x[0]
        n2 = x[1]
        while nmt[n1][n2] != 0:
            x = turn_value(sen_again)
            n1 = x[0]
            n2 = x[1]
        nmt[n1][n2] = "X"
        return nmt, countx, counto
    else:
        o = turn_value(sen_o)
        counto+=1
        n1 = o[0]
        n2 = o[1]
        while nmt[n1][n2] != 0:
            o = turn_value(sen_again)
            n1 = o[0]
            n2 = o[1]
        nmt[n1][n2] = "O"
        return nmt, countx, counto

def game_input(nmt):
    countx = 0
    counto = 0
    sen_x = "Player One is turn"
    sen_o = "Player Two is turn"
    sen_again = "This place is not empty. You can not put your sign in here."
    while 0 in nmt[0] or 0 in nmt[1] or 0 in nmt[2]:
        print(board_game(nmt))
        a = input_player_value(countx, counto, nmt, sen_x, sen_o, sen_again)
        nmt = a[0]
        if check_grid(nmt) == 'X':
            print(board_game(nmt))
            return 'Player One is Won!'
        if check_grid(nmt) == 'O':
            print(board_game(nmt))
            return 'Player Two is Won!'
        countx = a[1]
        counto = a[2]
    return "End"

nmt = [[0, 0, 0],
	   [0, 0, 0],
	   [0, 0, 0]]

game = game_input(nmt)
print(game)
