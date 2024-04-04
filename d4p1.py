import re

with open('inputs/scratchcards.txt') as sc:
    total = 0
    for line in sc:
        points = 0
        card = re.split(': | \\| ', line)
        win = card[1].split()
        have = card[2].split()
        for number in have:
            if number in win:
                points += points if points else 1
        total += points
print(total)
