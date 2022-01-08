"""https://adventofcode.com/2021 """

import numpy as np

file = open("input_day15.txt", "r")
cave_map = file.readlines()
file.close()

# cave_map = ['1163751742',
# '1381373672',
# '2136511328',
# '3694931569',
# '7463417111',
# '1319128137',
# '1359912421',
# '3125421639',
# '1293138521',
# '2311944581']

cave_map = [x.replace('\n', '') for x in cave_map]
cave_map = np.array([list(map(int, x.strip('\n'))) for x in cave_map]) 

# Part One
# Dijkstra Alg adapted from: https://levelup.gitconnected.com/dijkstras-shortest-path-algorithm-in-a-grid-eb505eb3a290
# assume starting position at 0,0 and ending position at max_val, max_val
def calcMinRiskPath(cave_map):
    max_val = cave_map.shape[0]
    
    dist_map = np.ones((max_val, max_val))*np.inf
    dist_map[0, 0] = 0
    origin_map = np.ones((max_val, max_val))*np.nan
    visited = np.zeros((max_val, max_val), dtype=bool)
    finished = False
    x, y = 0, 0
    count = 0
    
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    # Dijkstra Alg
    while not finished:
        for i in directions:
            new_x = x + i[0]
            new_y = y + i[1]
            if (new_x >= 0 and new_y >= 0 and new_x < max_val and new_y < max_val):
                if dist_map[new_x, new_y] > cave_map[new_x, new_y] + dist_map[x, y] and not visited[new_x, new_y]:
                    dist_map[new_x, new_y] = cave_map[new_x, new_y] + dist_map[x, y]
                    origin_map[new_x, new_y] = np.ravel_multi_index([x, y], (max_val, max_val))
                    
        visited[x, y] = True
        dist_maptemp = dist_map
        dist_maptemp[np.where(visited)] = np.inf
        # find next min path
        minpos = np.unravel_index(np.argmin(dist_maptemp), np.shape(dist_maptemp))
        
        x, y = minpos[0], minpos[1]
        
        if (x == max_val-1) and (y == max_val-1):
            finished = True
        count += 1
    
    
    # backtracking
    mattemp = cave_map.astype(float)
    x, y = max_val-1, max_val-1
    path = []
    mattemp[x, y] = np.nan
    
    while (x>0) or (y>0):
        path.append([x,y])
        next_xy = np.unravel_index(int(origin_map[x, y]), (max_val, max_val))
        x,y = next_xy[0], next_xy[1]
        mattemp[x, y] = np.nan
    path.append([x, y])
    
    # calculate risk
    risk = 0
    for i in path[:-1]:
        risk += cave_map[i[0], i[1]]
    
    return risk

risk = calcMinRiskPath(cave_map)
print('Total Min Risk Path: {}'.format(risk))

# Part Two
# Create new map
new_map = cave_map.copy()
prev_map = new_map.copy()
for i in range(1, 5):
    temp = prev_map + 1
    temp[temp > 9] = 1
    
    new_map = np.append(new_map, temp, axis=1)
    prev_map = temp

prev_map = new_map.copy()
for i in range(1, 5):
    temp = prev_map + 1
    temp[temp > 9] = 1
    
    new_map = np.append(new_map, temp, axis=0)
    prev_map = temp

risk = calcMinRiskPath(new_map)
print('Total Min Risk Path: {}'.format(risk))
