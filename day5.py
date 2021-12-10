import numpy as np

file = open("input_day5.txt", "r")
instructions = file.read().splitlines()
file.close()

# instructions = """0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2""".splitlines()

board_size = 5
board = np.zeros((board_size, board_size))

for i in instructions:
    coords = i.split('->')
    x1, y1 = [int(x) for x in coords[0].split(',')] 
    x2, y2 = [int(x) for x in coords[1].split(',')]
    
    if max(x1, x2, y1, y2)+1 > len(board):
        board_size = max(x1, x2, y1, y2)+1
        board = np.pad(board, [(0,board_size-len(board)), (0,board_size-len(board))], mode='constant')

    if y1 == y2:
        hori_dir = int((x1-x2)/abs(x1-x2))
        for j in range(x2, x1+hori_dir, hori_dir):
            board[y1][j] += 1
    elif x1 == x2:
        vert_dir = int((y1-y2)/abs(y1-y2))
        for k in range(y2, y1+vert_dir, vert_dir):
            board[k][x1] += 1        
    else:
        hori_dir = int((x1-x2)/abs(x1-x2))
        vert_dir = int((y1-y2)/abs(y1-y2))
        k = y2
        for j in range(x2, x1+hori_dir, hori_dir):
            board[k][j] += 1
            k += vert_dir

print((board >= 2).sum())    
            
    