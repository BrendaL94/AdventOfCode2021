"""https://adventofcode.com/2021 """


file = open("input_day10.txt", "r")
nav_subsystem = file.readlines()
file.close()

# Part One
syntax_points = {')':3, ']':57, '}':1197, '>':25137}

open_list = ['(', '[', '{', '<']
close_list = [')', ']', '}', '>']

incomplete_lines = nav_subsystem.copy()

illegal_char = []
for line in nav_subsystem:
    stack = []
    for i in line:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
                    stack.pop()
            else:
                incomplete_lines.remove(line)
                illegal_char.append(i)
                break

syntax_err_score = 0
for i in illegal_char:
    syntax_err_score += syntax_points.get(i)


# Part Two
complete_lines = []
for line in incomplete_lines:
    stack = []
    for i in line:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            stack.pop()
    stack.reverse()
    
    completed_line = []
    for i in stack:
        pos = open_list.index(i)
        completed_line.append(close_list[pos])
    complete_lines.append(''.join(completed_line))


autocomplete_points = {')':1, ']':2, '}':3, '>':4}
autocomplete_scores = []

for line in complete_lines:
    score = 0
    for i in line:
        score = score * 5 + autocomplete_points.get(i)
    autocomplete_scores.append(score)

autocomplete_scores.sort()

print('Middle score: {}'.format(autocomplete_scores[int(len(autocomplete_scores)/2-0.5)]))
