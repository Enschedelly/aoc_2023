import numpy

sum = 0
matrix = []
with open('inputs/engine_schematic.txt') as es:
    for line in es:  # Put the entire engine schematic in a matrix structure
        row = []
        for char in line:
            row.append(char)
        matrix.append(row)

for row_idx in range(len(matrix)):
    for col_idx in range(len(matrix[row_idx])):  # For each character in the engine schematic
        touching_numbers = []
        if matrix[row_idx][col_idx] == '*':  # If the character is an asteriks we loop through all adjecent characters
            for row in range(row_idx-1, row_idx+2):  
                end_char = 0
                for char in range(col_idx-1, col_idx+2):
                    if char < end_char:  # If we already checked this character in an earlier loop, we skip it
                        continue
                    if matrix[row][char].isdigit():  # If the character is a digit
                        try:
                            step = 0 
                            still_digit = True
                            number = ''
                            while still_digit:  # We go left to see where the number starts
                                if matrix[row][char + step].isdigit():
                                    step -= 1
                                else:
                                    still_digit = False 
                            step += 1
                            still_digit = True                                          
                            while still_digit:  # Then we go right and add each character of the number to the variable.
                                if matrix[row][char + step].isdigit():
                                    number += matrix[row][char + step]
                                    step += 1
                                else:
                                    still_digit = False
                            end_char = char + step  # We indicate that we already checked additional characters, so they can be skipped.
                            touching_numbers.append(int(number))  # We append the number to the list of all adjecent numbers.
                        except IndexError:  # If the asteriks is on an edge, we ignore index out of bounds.
                            pass
            
        if len(touching_numbers) == 2:  # If an asteriks has exactly two adjecent numbers, we add its product to the sum.
            sum += numpy.prod(touching_numbers) 
        touching_numbers = []
print(sum)
