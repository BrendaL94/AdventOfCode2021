file = open("input_day7.txt", "r")
crab_pos = file.read().split(',')
crab_pos = [int(x) for x in crab_pos] 
file.close()

# crab_pos = [16,1,2,0,4,2,7,1,2,14]

# part one
min_fuel = max(crab_pos)**10
min_pos = -1
for i in range(0, len(crab_pos)):
    pos_temp = [abs(x-i) for x in crab_pos]
    if min_fuel > sum(pos_temp):
        min_fuel = sum(pos_temp)
        min_pos = i

print('Least amount of fuel {} at position {}'.format(min_fuel, min_pos))

# part two
min_fuel = max(crab_pos)**10
min_pos = -1
for i in range(0, len(crab_pos)):
    # 1+2+3+...n = n*(n+1)/2
    pos_temp = [abs(x-i)*(abs(x-i)+1)/2 for x in crab_pos]
    if min_fuel > sum(pos_temp):
        min_fuel = sum(pos_temp)
        min_pos = i

print('Least amount of fuel {:.0f} at position {}'.format(min_fuel, min_pos))
