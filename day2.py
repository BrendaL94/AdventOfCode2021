# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 17:26:25 2021

@author: ABBL257
"""

horizontal = 0
depth = 0
aim = 0

file = open("input_day2.txt", "r")
movement = file.read().splitlines()
file.close()

for i in range(0, len(movement)):
    instruction = movement[i].split(' ')
    if instruction[0] == 'forward':
        horizontal = horizontal + int(instruction[1])
        depth = depth + aim * int(instruction[1])
    elif instruction[0] == 'down':
        aim = aim + int(instruction[1])
    elif instruction[0] == 'up':
        aim = aim - int(instruction[1])
        
print(depth * horizontal)

