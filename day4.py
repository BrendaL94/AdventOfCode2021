"""https://adventofcode.com/2021"""
import numpy as np

file = open("input_day4.txt", "r")
bingo_numbers= [int(x) for x in file.readline().strip().split(',')]
bingo_boards = file.read()
file.close()

# part 1
boards = bingo_boards.strip().split('\n\n')
board_array = []
num_boards = 0
for i in boards:
    line = i.replace('  ', ' ').split('\n')
    num_boards += 1
    for j in line:
        board_array.append([int(x) for x in j.strip().split(' ')])
        
cross_out = np.array(board_array.copy())
for i in bingo_numbers:
    
    cross_out = np.where(cross_out == i, -1, cross_out)
    
    for j in np.reshape(np.ravel(cross_out), (num_boards,5,5)):
        if any(np.sum(j, axis=1) == -5) or (any(np.sum(j, axis=0) == -5)):
            mask = j != -1
            print('Sum of Board: ' + str(sum(j[mask])))
            print('Last Number Called: '+ str(i))
            print('Final Score: ' + str(sum(j[mask] * i)))
            break
        else: 
            continue
        break
    else: continue

    break
    
# part 2
cross_out = np.array(board_array.copy())
board_numbers = list(np.arange(0, num_boards))
winning_order = []

for i in bingo_numbers:
    cross_out = np.where(cross_out == i, -1, cross_out)
    
    for k in board_numbers:
        j = np.reshape(np.ravel(cross_out), (num_boards,5,5))[k]
        if ((any(np.sum(j, axis=1) == -5) or (any(np.sum(j, axis=0) == -5))) and (k not in winning_order)):
            winning_order.append(k)
            board_numbers.remove(k)
            
    # check if it's the last winning board or if we've reached the end of bingo numbers
    if ((len(winning_order) == num_boards) or (i == bingo_numbers[-1])):
        last_board = np.reshape(np.ravel(cross_out), (num_boards,5,5))[winning_order[-1]]
        mask = last_board != -1
        print('Sum of Board: ' + str(sum(last_board[mask])))
        print('Last Number Called: '+ str(i))
        print('Final Score: ' + str(sum(last_board[mask] * i)))
        break
