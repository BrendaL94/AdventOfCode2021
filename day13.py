"""https://adventofcode.com/2021 """

import numpy as np

file = open("input_day13.txt", "r")
f = file.read()
file.close()

f = f.split('\n\n')
dot_map = f[0].split('\n')
instructions = f[1].split('\n')
instructions = [x.strip('fold along ') for x in instructions]

# find board dimensions
max_x = 0
max_y = 0
for i in instructions:
    if (max_x != 0 and max_y != 0):
        break
    fold_direction = i.split('=')[0]
    fold_amount = int(i.split('=')[1])
    if (fold_direction == 'y' and max_y == 0):
        max_y = (fold_amount * 2) + 1
    elif (fold_direction == 'x' and max_x == 0):
        max_x = (fold_amount * 2) + 1

for num, coord in enumerate(dot_map):
    x = int(coord.split(',')[0])
    y = int(coord.split(',')[1])
    dot_map[num] = (x, y)

# create board
board = []
for i in range(0, max_y):
    board.append(['.'] * max_x)
board = np.array(board)

# fill in board with '#'
for i in dot_map:
    board[i[1]][i[0]] = '#'

# fold instructions
for i in instructions:
    fold_direction = i.split('=')[0]
    fold_amount = int(i.split('=')[1])
    
    new_board = []
    # fold horizontally
    if fold_direction == 'y':
        for row in range(0, fold_amount):
            new_board.append(['#' if (a_ == '#' or '#' == b_) else '.' for a_, b_ in zip(board[row], board[-(row+1)])])
    # fold vertically
    elif fold_direction == 'x':
        for row in range(0, len(board)):
            new_board.append(['#' if ('#' == a_ or '#' == b_) else '.' for a_, b_ in zip(board[row][:fold_amount], board[row][fold_amount:][::-1])])
                
    new_board = np.array(new_board)
    board = new_board.copy()

mask = []
for i in range(0, len(board)):
    mask.append([True if '#' in x else False for x in list(board[i])])
mask = np.array(mask)

print('Number of dots visible: {}'.format(mask.sum()))

def printBoard(board):
    for row in board:
        print(''.join(row))

printBoard(board)
