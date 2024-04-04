import re

with open('inputs/scratchcards.txt') as sc:
    total = 0
    for line in sc:  # For each scratchcard in the game
        points = 0
        card = re.split(': | \\| ', line)  # We make an array with [card id, winning number, numbers you have]
        win = card[1].split()
        have = card[2].split()
        for number in win:  # For each number in winning numbers
            if number in have:  # If we also have that number, we double our points
                points += points if points else 1  # If this is our first point, we set points to 1
        total += points  # We add our points to the total
print(total)
