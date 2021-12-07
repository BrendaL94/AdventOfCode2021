"""https://adventofcode.com/2021"""

file = open("input_day3.txt", "r")
binary = file.read().splitlines()
file.close()

# part one
gamma_rate = ''
epsilon_rate = ''

for i in range(0, len(binary[0])):
    lst = [int(x[i]) for x in binary]
    if sum(lst) > len(lst)/2:
        gamma_rate = gamma_rate + '1'
        epsilon_rate = epsilon_rate + '0'
    else:
        gamma_rate = gamma_rate + '0'
        epsilon_rate = epsilon_rate + '1'

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)
power = gamma_rate * epsilon_rate
print(power)

# part two
def calc_rating(binary, keep, discard):
    for i in range(0, len(binary[0])):
        lst = [int(x[i]) for x in binary]
        
        if sum(lst) >= len(lst)/2:
            binary = [x for x in binary if x[i] == keep]
        else:
            binary = [x for x in binary if x[i] == discard]
    
        if len(binary) == 1:
            return int(binary[0], 2)

oxygen_generator_rating = calc_rating(binary, '1', '0')
co2_scrubber_rating = calc_rating(binary, '0', '1')


life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    
print(life_support_rating)


