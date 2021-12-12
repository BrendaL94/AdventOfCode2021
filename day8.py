"""https://adventofcode.com/2021"""

import numpy as np

file = open("input_day8.txt", "r")
inputs = file.readlines() 
file.close()

# inputs = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""".splitlines()

total = 0

def find_diff(str1, str2):
    return list(set(str1) - set(str2))

for i in inputs:
    seven_seg = {'a':'', 'b':'', 'c':'', 'd':'', 'e':'', 'f':'', 'g':''}
    numbers = {0:'', 1:'', 2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:'', 9:''}

    outputs = i.split(' | ')[0].split(' ')

    # find 1,4,7,8 
    numbers[1] = [x for x in outputs if len(x) == 2][0]
    numbers[7] = [x for x in outputs if len(x) == 3][0]
    numbers[4] = [x for x in outputs if len(x) == 4][0]
    numbers[8] = [x for x in outputs if len(x) == 7][0]

    seven_seg['a'] = find_diff(numbers[7], numbers[1])[0]

    # find 6
    find_6_letters = [x for x in outputs if len(x) == 6]
    for j in find_6_letters:
        if len(find_diff(numbers[1], j)) == 1:
            numbers[6] = j
            seven_seg['c'] = find_diff(numbers[1], j)[0]

    # find what makes up 1
    seven_seg['f'] = find_diff(numbers[1], seven_seg['c'])[0]

    # find 5
    find_5_letters = [x for x in outputs if len(x) == 5]
    for j in find_5_letters:
        if seven_seg['c']  not in j:
            numbers[5] = j
            seven_seg['e'] = find_diff(numbers[6], numbers[5])[0]   

    # find 9
    for j in find_6_letters:
        if seven_seg['e']  not in j:
            numbers[9] = j
        
    # find 0
    find_6_letters.remove(numbers[6])
    find_6_letters.remove(numbers[9])
    numbers[0] = find_6_letters[0]
    seven_seg['d'] = find_diff(numbers[8], numbers[0])[0]
    seven_seg['b'] = find_diff(numbers[4], (seven_seg['c'] + seven_seg['d']+seven_seg['f']))[0]
    seven_seg['g'] = find_diff(numbers[8], ''.join(seven_seg.values()))[0]

    # find 2
    for j in find_5_letters:
        if seven_seg['e'] in j:
            numbers[2] = j
    
    # find 3
    find_5_letters.remove(numbers[2])
    find_5_letters.remove(numbers[5])
    numbers[3] = find_5_letters[0]

    # find number
    number = []
    for j in i.strip().split(' | ')[1].split(' '):
        for k in numbers:
            if set(numbers[k]) == set(j):
                number.append(k)
                break

    total += int(''.join([str(x) for x in number]))

print(total)
