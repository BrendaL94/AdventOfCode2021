"""https://adventofcode.com/2021"""

file = open("input_day1.txt", "r")
depth = file.read().splitlines()
depth = [int(i) for i in depth]
file.close()

# part one
increased_counter = 0
for i in range(1, len(depth)):
    if depth[i] > depth[i-1]:
        increased_counter+=1
    
print(increased_counter)

# part two
increased_counter = 0
for i in range(0, len(depth)):
    if sum(depth[i:i+3]) < sum(depth[i+1:i+1+3]):
        increased_counter+=1
        
print(increased_counter)

