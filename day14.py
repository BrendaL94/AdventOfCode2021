"""https://adventofcode.com/2021 """

from collections import Counter

file = open("input_day14.txt", "r")
f = file.read()
file.close()

# f = """NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C"""

f = f.split('\n\n')
template = [char for char in f[0]]
rules = f[1].split('\n')

rules_dict = {}
for num, rule in enumerate(rules):
    splitRule = rule.split(' -> ')
    rules_dict[splitRule[0]] = splitRule[1]

# Part One
for i in range(10):
    insert_dict = {}
    for j in range(len(template) - 1):
        try:
            insert_dict[j] = rules_dict.get(template[j] + template[j+1])
        except:
            pass      

    sortedDict = sorted(insert_dict.keys(), reverse=True)
    for j in sortedDict:
        template.insert(j+1, insert_dict[j])

counter = Counter(template).most_common()
print(counter[0][1] - counter[-1][1])

# Part Two
digram_dict = {}
letters_dict = Counter(template)

for j in range(len(template) - 1):
    digram = template[j] + template[j+1]
    if digram in digram_dict:
        digram_dict[digram] += 1
    else:
        digram_dict[digram] = 1

for i in range(10, 40):
    insert_dict = {}
    remove_dict = {}
    for digram in rules_dict:

        if (digram in digram_dict) and (digram_dict[digram] > 0):
            num_insertions = digram_dict[digram]
            insert_val = rules_dict[digram]

            # Add first new digram 
            if (digram[0] + insert_val) in insert_dict:
                insert_dict[digram[0] + insert_val] += num_insertions
            else:
                insert_dict[digram[0] + insert_val] = num_insertions

            # Add second new digram
            if (insert_val + digram[1]) in insert_dict:
                insert_dict[insert_val + digram[1]] += num_insertions
            else:
                insert_dict[insert_val + digram[1]] = num_insertions

            # All new insert_val added
            if insert_val in letters_dict:
                letters_dict[insert_val] += num_insertions
            else:
                letters_dict[insert_val] = num_insertions
            
            # Resets digram amount to 0
            digram_dict[digram] = 0

    # Adding new pairs
    digram_dict = {k: insert_dict.get(k, 0) + digram_dict.get(k, 0) for k in set(insert_dict) | set(digram_dict)}

letters_dict = letters_dict.most_common()
print(letters_dict[0][1] - letters_dict[-1][1])
