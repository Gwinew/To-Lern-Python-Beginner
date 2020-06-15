'''
This is exercise is Part 3 of 4 of the Tic Tac Toe exercise series.

In a previous exercise we explored the idea of using a list of lists as a “data structure”
to store information about a tic tac toe game. In a tic tac toe game,
the “game server” needs to know where the Xs and Os are in the board,
to know whether player 1 or player 2 (or whoever is X and O won).

There has also been an exercise about drawing the actual tic tac toe gameboard using text characters.

The next logical step is to deal with handling user input.
When a player (say player 1, who is X) wants to place an X on the screen,
they can’t just click on a terminal. So we are going to approximate this clicking
simply by asking the user for a coordinate of where they want to place their piece.

As a reminder, our tic tac toe game is really a list of lists.
The game starts out with an empty game board like this:

game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]
The computer asks Player 1 (X) what their move is (in the format row,col),
and say they type 1,3. Then the game would print out

game = [[0, 0, X],
	[0, 0, 0],
	[0, 0, 0]]
And ask Player 2 for their move, printing an O in that place.

Things to note:

For this exercise, assume that player 1 (the first player to move)
will always be X and player 2 (the second player) will always be O.
Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of (0, 0).
To people who don’t program, starting to count at 0 is a strange concept,
so it is better for the user experience if the row counts and column counts start at 1. This is not required,
but whichever way you choose to implement this, it should be explained to the player.
Ask the user to enter coordinates in the form “row,col” - a number,
then a comma, then a number. Then you can use your
Python skills to figure out which row and column they want their piece to be in.
Don’t worry about checking whether someone won the game,
but if a player tries to put a piece in a game
position where there already is another piece, do not allow the piece to go there.

    Bonus:

        For the “standard” exercise, don’t worry about “ending” the game - no need to keep track of
        how many squares are full. In a bonus version, keep track of how many squares are
        full and automatically stop asking for moves when there are no more valid moves.
'''
"""
nmt = [[0, 0, 0],
	   [0, 0, 0],
	   [0, 0, 0]]
countx = 0
county = 0
while 0 in nmt[0] or 0 in nmt[1] or 0 in nmt[2]:
	if countx <= county:
		x = input('Player One, please enter:\n')
		countx+=1
		value_list = x.split(',')
		num1 = int(value_list[0])-1
		num2 = int(value_list[1])-1
		while nmt[num1][num2] != 0:
			x = input('This place have value, eneter different:\n')
			value_list = x.split(',')
			num1 = int(value_list[0])-1
			num2 = int(value_list[1])-1
		nmt[num1][num2] = "X"
	else:
		o = input('Player Two, please enter:\n')
		county+=1
		value_list = o.split(',')
		num1 = int(value_list[0])-1
		num2 = int(value_list[1])-1
		while nmt[num1][num2] != 0:
			o = input('This place have value, eneter different:\n')
			value_list = o.split(',')
			num1 = int(value_list[0])-1
			num2 = int(value_list[1])-1
		nmt[num1][num2] = "O"
	print(nmt)
print('End')
"""
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
		print(nmt)
		a = input_player_value(countx, counto, nmt, sen_x, sen_o, sen_again)
		nmt = a[0]
		countx = a[1]
		counto = a[2]
	return "End"

nmt = [[0, 0, 0],
	   [0, 0, 0],
	   [0, 0, 0]]

game = game_input(nmt)
print(game)
