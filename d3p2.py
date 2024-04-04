import numpy

sum = 0
matrix = []
with open('inputs/engine_schematic.txt') as es:
    for line in es:
        row = []
        for char in line:
            row.append(char)
        matrix.append(row)

for row_idx in range(len(matrix)):
    for col_idx in range(len(matrix[row_idx])):
        touching_numbers = []
        if matrix[row_idx][col_idx] == '*':
            print(' HIT')
            for row in range(row_idx-1, row_idx+2):
                end_char = 0
                for char in range(col_idx-1, col_idx+2):
                    if char < end_char:
                        continue
                    if matrix[row][char].isdigit():
                        try:
                            step = 0 
                            still_digit = True
                            number = ''
                            while still_digit:
                                if matrix[row][char + step].isdigit():
                                    step -= 1
                                else:
                                    still_digit = False 
                            step += 1
                            still_digit = True                                          
                            while still_digit:
                                if matrix[row][char + step].isdigit():
                                    number += matrix[row][char + step]
                                    step += 1
                                else:
                                    still_digit = False
                            end_char = char + step
                            print(number)
                            if number:
                                touching_numbers.append(int(number))
                            print(touching_numbers)
                        except IndexError:
                            pass
            
        if len(touching_numbers) == 2:
            sum += numpy.prod(touching_numbers) 
        touching_numbers = []
print(sum)
