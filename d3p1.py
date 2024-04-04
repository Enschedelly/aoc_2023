sum = 0
matrix = []
with open('inputs/engine_schematic.txt') as es:
    for line in es:  # Put the entire engine schematic in a matrix structure.
        row = []
        for char in line:
            row.append(char)
        matrix.append(row)

for row_idx in range(len(matrix)):
    end_col = 0
    for col_idx in range(len(matrix[row_idx])):  # For each character in the engine schematic
        if col_idx < end_col:  # We check if we already scanned additional characters within the previous loop(s)
            continue           # If so, we continue to the next character
        if matrix[row_idx][col_idx].isdigit():  # We check if the current character is a digit, else we go to the next character
            still_digit = True
            number = matrix[row_idx][col_idx]  # Get the first digit of the number
            step = 1
            end_col = col_idx  
            while still_digit:  # We want to collect the entire number
                if matrix[row_idx][col_idx + step].isdigit():  # If the next character is also a digit, append it to the number
                    number += matrix[row_idx][col_idx + step]  # and check the next character
                    step += 1
                else:
                    still_digit = False  # Else we break out of the loop.
            valid = False
            for row in range(row_idx-1, row_idx+2):  # We now loop through all to the number adjecent characters.
                for char in range(col_idx-1, col_idx+step+1):
                    try:  # If the character is adjecent to something else than a number, period or break, it is valid.                                               
                        if not matrix[row][char].isdigit() and not matrix[row][char] == "." and not matrix[row][char] == "\n":
                            valid = True
                            break
                    except IndexError:  # If the number is on an edge, we ignore an index out of bounds error.
                        pass
            if valid:  # If the number is valid, we add it to the sum of part numbers.
                sum += int(number)       
            end_col += step  # We indicate that we already checked more characters in this iteration, so they can be skipped.
            
print(sum)



