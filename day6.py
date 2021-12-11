"""https://adventofcode.com/2021"""

import numpy as np
from collections import deque

file = open("input_day6.txt", "r")
fish_list = file.read().split(',')
fish_list = [int(x) for x in fish_list] 
file.close()

#fish_list = [3,4,3,1,2]
days = 256

fish_tracker = np.arange(0, 9, dtype='int64')
for i in range(0, 9):
    fish_tracker[i] = (np.array(fish_list)==i).sum()

for _ in range(0, days):
    num_new_fish = fish_tracker[0]

    fish_tracker = deque(fish_tracker)
    fish_tracker.rotate(-1)
    fish_tracker = list(fish_tracker)
    
    # add number of new fishes to day 8 and
    # add number of old fishes that were on day 0 to reset at day 6
    fish_tracker[8] = num_new_fish
    fish_tracker[6] += num_new_fish

print('Total number of lanternfishes after {} days: {:,}'.format(days, sum(fish_tracker)))
