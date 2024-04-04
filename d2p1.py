red = 12
green = 13
blue = 14

sum = 0
with open('inputs/block_puzzle.txt') as bp:
    for line in bp:  # For each game in the block puzzle
        game_id = int(line.split()[1][0:-1])  # Get the game ID and the draws
        draws = line.split(': ')[1][:-1]
        possible = True
        for draw in draws.split('; '):  # For each draw in the game
            for cubes in draw.split(', '):  # For each cube colour in a draw
                number, colour = cubes.split()[0], cubes.split()[1]  # If the number of cubes drawn is larger than the amount present
                if (colour == 'red' and int(number) > red) or (colour == 'green' and int(number) > green) or (colour == 'blue' and int(number) > blue):
                    possible = False  # Set this game to impossible
        if possible:
            sum += game_id  # Else we add the game ID to the sum of all IDs.

print(sum)
                    