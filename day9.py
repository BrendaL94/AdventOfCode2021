"""https://adventofcode.com/2021 """

import numpy as np

file = open("input_day9.txt", "r")
heatmap = file.readlines() 
file.close()

# heatmap = ['2199943210',
# '3987894921',
# '9856789892',
# '8767896789',
# '9899965678']

heatmap = [x.replace('\n', '') for x in heatmap]

# part one
# pad with 9 on heatmap so comparison won't go out of bounds
heatmap = ['9' + x + '9' for x in heatmap]
heatmap.insert(0, '9' * len(heatmap[0]))
heatmap.append('9' * len(heatmap[0]))

lowestPoints = []
lowestPointsPos = []
# check horizontal 
for i in range(1, len(heatmap)-1):
    # check vertical
    for j in range(1, len(heatmap[0])-1):
        current_num = heatmap[i][j]
        # check boundaries
        if (heatmap[i-1][j] > current_num) & (heatmap[i+1][j] > current_num) & \
            (heatmap[i][j-1] > current_num) & (heatmap[i][j+1] > current_num):
            lowestPoints.append(current_num)
            lowestPointsPos.append((i, j))

risk_level = [int(x)+1 for x in lowestPoints]
print('Risk Level: {}'.format(sum(risk_level)))

# part two
# using recursion of flood fill
basin_sizes = []
def floodFill(x, y, boundary):
    if (x < 0 or x >= len(heatmap) or y < 0 or y >= len(heatmap[0]) or int(heatmap[x][y]) == boundary):
        return 

    heatmap[x] = heatmap[x][:y] + boundary + heatmap[x][y+1:]
    size_of_basin.append(1)
    
    # recur for up down left right
    floodFill(x+1, y, boundary)
    floodFill(x-1, y, boundary)
    floodFill(x, y+1, boundary)
    floodFill(x, y-1, boundary)


for i, j in lowestPointsPos:
    size_of_basin = []
    floodFill(i, j, '9')
    
    basin_sizes.append(len(size_of_basin))
  
basin_sizes.sort()
print('Three largest basins: {}'.format(basin_sizes[-3:]))
print('Product of three largest basins: {}'.format(np.prod(basin_sizes[-3:])))
