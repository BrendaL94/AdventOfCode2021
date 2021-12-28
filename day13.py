"""https://adventofcode.com/2021 """

import numpy as np

file = open("input_day13.txt", "r")
f = file.read()
file.close()

# f = """6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0

# fold along y=7
# fold along x=5"""

f = f.split('\n\n')
dot_map = f[0].split('\n')
instructions = f[1].split('\n')
instructions = [x.strip('fold along ') for x in instructions]

# find board dimensions
max_x = 0
max_y = 0

for num, coord in enumerate(dot_map):
    x = int(coord.split(',')[0])
    y = int(coord.split(',')[1])
    
    dot_map[num] = (x, y)
    
    if x > max_x:
        max_x = x
    elif y > max_y:
        max_y = y
    
# create board
board = []
max_x += 1
max_y += 1
for i in range(0, max_y):
    board.append(['.'] * max_x)
board = np.array(board)

# fill in board with '#'
for i in dot_map:
    board[i[1]][i[0]] = '#'

#board size 895 1310

# fold instructions
for i in instructions[:1]:
    fold_direction = i.split('=')[0]
    fold_amount = int(i.split('=')[1])
    
    new_board = []
    # fold horizontally
    if fold_direction == 'y':
        for row in range(0, fold_amount):
            new_board.append(["{}{}".format(a_, b_) for a_, b_ in zip(board[row], board[-(row+1)])])
    # fold vertically
    elif fold_direction == 'x':
        for row in range(0, len(board)):
            new_board.append(["{}{}".format(a_, b_) for a_, b_ in zip(board[row][:fold_amount], board[row][fold_amount:][::-1])])
    new_board = np.array(new_board)
    board = new_board.copy()

# clean up board, change to just 'x' or '.'
new_board = []
mask = []
for i in range(0, len(board)):
    new_board.append(['#' if '#' in x else '.' for x in list(board[i])])
    mask.append([True if '#' in x else False for x in list(board[i])])
new_board = np.array(new_board)
mask = np.array(mask)

print('Number of dots visible: {}'.format(mask.sum()))
