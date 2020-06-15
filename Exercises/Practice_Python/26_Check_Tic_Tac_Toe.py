'''
This exercise is Part 2 of 4 of the Tica Tac Toe exercise series.

As you may have guessed, we are trying to build up to a full tic-tac-toe
board. However, this is significantly more than half an hour of coding,
so we're doing it in pieces.

Today, we will simply focus on checking whether someone has WON a game of
Tic Tac Toe, not worrying abount how the moves were made.

If a game of Tic Tac Toe is represented as a list of lists, like so:

game = [[1,2,0],
    [2,1,0],
    [2,1,1]]

where a 0 means an empty square , a 1 means that player 1 put their token
in that space, and a 2 means that player 2 put their token in that space.

Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe
game board, tell me whether anyone has won, and tell me which player won,
if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal.
Don't worry about the case where TWO people have won - assume that in every
board there will only be one winner.

Here are some more examlpes to work with:

winner_is_2 = [[2,2,0],
    [2,1,0],
    [2,1,1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]
'''

def check_grid(nmt):
    #row
    for i in range(3):
        num = set(nmt[i])
        if len(num)==1 and nmt[i][0] != 0:
            print(num, len(num))
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

game = [[1,2,0],
    [0,0,0],
    [0,0,0]]

player = check_grid(game)
if player != 0:
    print(f'Player {player} is WON!')
else:
    print('Draw!')
