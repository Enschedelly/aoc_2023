red = 12
green = 13
blue = 14

sum = 0
with open('inputs/block_puzzle.txt') as bp:
    for line in bp:
        draws = line.split(': ')[1][:-1]
        possible = [0, 0, 0]
        power = 0
        for draw in draws.split('; '):
            for cubes in draw.split(', '):
                number, colour = cubes.split()[0], cubes.split()[1]
                if colour == 'red':
                    if int(number) > possible[0]:
                        possible[0] = int(number)
                if colour == 'green':
                    if int(number) > possible[1]:
                        possible[1] = int(number)
                if colour == 'blue':
                    if int(number) > possible[2]:
                        possible[2] = int(number)
        power = possible[0] * possible[1] * possible[2]
        sum += power

print(sum)
                  