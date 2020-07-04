import numpy as np
import random


def create_board():
    return np.zeros((3, 3), dtype=int)
'''
def place(board, player, position):
    if board[position[0]][position[1]] == 0:
        board[position[0]][position[1]] = player
        return board
    return board
'''
def place(board, player, position):
    if board[position] == 0:
        board[position] = player
        return board
    return board
'''
def possibilities(board):
    b = np.where(board == 0)
    c= []
    for i in range(len(b[0])):
        c.append((b[0][i], b[1][i]))
    return c
'''
def possibilities(board):
    return list(zip(*np.where(board == 0)))

def random_place(board, player):
    selection = possibilities(board)
    random_position = random.choice(selection)
    return place(board, player, random_position), random_position

def row_win(board, player):
    for i in range(len(board)):
        if np.all(board[i]==player):
            return True
    return False

def col_win(board, player):
    for i in range(len(board[0])):
        if np.all(board[:, i]==player):
            return True
    return False

def diag_win(board, player):
    if np.all(np.diag(board)==player) or np.all(np.diag(np.fliplr(board))==player):
        return True
    return False

def evaluate(board):
    winner = 0
    for player in [1,2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
            break

    if np.all(board != 0) and winner ==0:
        winner = -1
    return winner

def play_game():
    c = True
    board = create_board()
    while c == True:
        for player in [1,2]:
            random_place(board, player)
            won = evaluate(board)
            if won != 0:
                c = False
                break
    return won

def play_strategic_game():
    c = True
    board = create_board()
    place(board, 1, (1,1))
    while c == True:
        for player in [2,1]:
            random_place(board, player)
            won = evaluate(board)
            if won != 0:
                c = False
                break
    return won

#board = create_board()
#place(board, 1,(0,0))
#print(board)
#print(possibilities(board))
#random.seed(1)
#print(random_place(board, 2))

#random.seed(1)
#board = create_board()
#play_1 = []
#play_2 = []
#for i in range(3):
#    player = 1
#    board, count_1 = random_place(board, player)
#    play_1.append(count_1)
#    player = 2
#    board, count_2 = random_place(board, player)
#    play_2.append(count_2)
#print(board)
##print(play_1)
##print(play_2)
#print(row_win(board, 1))
#print(col_win(board, 1))
#board[1,1] = 2
#print(board)
#print(diag_win(board, 2))
#print(evaluate(board))

#result = []
random.seed(1)
#for i in range(1000):

#    k = play_game()
#    result.append(k)
result = [play_strategic_game() for k in range(1000)]

print(result.count(1))
print(result.count(-1))
print(result.count(2))
print(len(result))
