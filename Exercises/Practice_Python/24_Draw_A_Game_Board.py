'''
This exercise is Part 1 of 4 of the Tic Tac Toe exercise series.

Time for some fake graphics! Let's say we want to draw game
boards that look like this.

 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---

 This one is 3x3 (like in tic tac toe). Obviously, they come in
 many other sizes (8x8 for chess, 19x19 for Go, and many more).

 Ask the user what size game board they want to draw, and draw it
 for them to the screen using Python's print statement.

 Remember that in Python 3, printing to the screen is accomplished by

 print('Thing to show on screen')
'''

def border_up_down_line(num_x):
    return ' --- '+'--- '*(num_x-1)

def border_side_line(num_x):
    return '|   |'+'   |'*(num_x-1)

num_x = int(input('Please give the number of x-axis:\n'))
num_y = int(input('Please give the number of y-axis:\n'))

print(border_up_down_line(num_x))
for i in range(num_y):
    print(border_side_line(num_x))
    print(border_up_down_line(num_x))
