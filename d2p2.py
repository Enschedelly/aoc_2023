red = 12
green = 13
blue = 14

sum = 0
with open('inputs/block_puzzle.txt') as bp:
    for line in bp:  # For each game in the block puzzle
        draws = line.split(': ')[1][:-1]  # Get the draws
        possible = [0, 0, 0]  # New array containing the lowest possible of [red, green, blue] blocks
        power = 0
        for draw in draws.split('; '):  # For each draw in the game
            for cubes in draw.split(', '):  # For each cube colour in a draw
                number, colour = cubes.split()[0], cubes.split()[1]
                if colour == 'red':  # For each colour, check if the amount in the current draw is higher than currently set.
                    if int(number) > possible[0]:
                        possible[0] = int(number)  # If so, put the amount of the current draw in the array.
                if colour == 'green':
                    if int(number) > possible[1]:
                        possible[1] = int(number)
                if colour == 'blue':
                    if int(number) > possible[2]:
                        possible[2] = int(number)
        power = possible[0] * possible[1] * possible[2]  # Calculate the power of this minimum required amount of coloured cubes
        sum += power  # Add that to the sum

print(sum)
                  