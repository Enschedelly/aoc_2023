red = 12
green = 13
blue = 14

sum = 0
with open('inputs/block_puzzle.txt') as bp:
    for line in bp:
        game_id = int(line.split()[1][0:-1])
        draws = line.split(': ')[1][:-1]
        possible = True
        for draw in draws.split('; '):
            for cubes in draw.split(', '):
                number, colour = cubes.split()[0], cubes.split()[1]
                if (colour == 'red' and int(number) > red) or (colour == 'green' and int(number) > green) or (colour == 'blue' and int(number) > blue):
                    possible = False
        if possible:
            sum += game_id

print(sum)
                    