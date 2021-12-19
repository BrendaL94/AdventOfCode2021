"""https://adventofcode.com/2021 """

import numpy as np

file = open("input_day11.txt", "r")
oct_map = file.readlines()
file.close()

# oct_map = """5483143223,
# 2745854711,
# 5264556173,
# 6141336146,
# 6357385478,
# 4167524645,
# 2176841721,
# 6882881134,
# 4846848554,
# 5283751526""".split(',')

oct_map = np.array([list(map(int, x.strip('\n'))) for x in oct_map])

# Part One
directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

def recur_check(x_pos, y_pos):       
    for i in directions:
        new_x = x_pos + i[0]
        new_y = y_pos + i[1]
        if (new_x >= 0 and new_y >= 0 and new_x < len(oct_map) and new_y < len(oct_map[0])):
            oct_map[new_x][new_y] += 1
            if ((oct_map[new_x][new_y] > 9) and ((new_x, new_y) not in flashed_pos)):
                flashed_pos.append((new_x, new_y))
                recur_check(new_x, new_y)


flash_count = []
for _ in range(0, 100):
    # step 1: add energy to all octopus by 1
    oct_map += 1
    
    # step 2: check if there are any flashes (>9)
    mask = oct_map > 9
    x, y = np.where(mask)
    flashed_pos = []
    for i, j in zip(x, y):
        if (i, j) not in flashed_pos:
            flashed_pos.append((i, j))
            recur_check(i, j)
        
    flash_count.append(len(flashed_pos))
    
    # step 3: change all flashed back to 0
    mask = oct_map > 9
    oct_map[mask] = 0

print('Number of flashes: {}'.format(sum(flash_count)))


# Part Two
sync_count = 0
not_synced = True
while (not_synced):
    sync_count += 1
    # step 1: add energy to all octopus by 1
    oct_map += 1
    
    # step 2: check if there are any flashes (>9)
    mask = oct_map > 9
    x, y = np.where(mask)
    flashed_pos = []
    for i, j in zip(x, y):
        if (i, j) not in flashed_pos:
            flashed_pos.append((i, j))
            recur_check(i, j)
        
    # step 3: change all flashed back to 0
    mask = oct_map > 9
    oct_map[mask] = 0
    
    if oct_map.sum() == 0:
        not_synced = False

print('First sync step: {}'.format(sync_count))
