

sum = 0
matrix = []
with open('inputs/test_input.txt') as es:
    for line in es:
        row = []
        for char in line:
            row.append(char)
        matrix.append(row)

for row_idx in range(len(matrix)):
    end_col = 0
    for col_idx in range(len(matrix[row_idx])):
        if col_idx < end_col:
            continue
        if matrix[row_idx][col_idx].isdigit():
            still_digit = True
            number = matrix[row_idx][col_idx]
            step = 1
            end_col = col_idx
            while still_digit:
                if matrix[row_idx][col_idx + step].isdigit():
                    number += matrix[row_idx][col_idx + step]
                    step += 1
                else:
                    still_digit = False
            valid = False
            for row in range(row_idx-1, row_idx+2):
                for char in range(col_idx-1, col_idx+step+1):
                    try:                                              
                        if not matrix[row][char].isdigit() and not matrix[row][char] == "." and not matrix[row][char] == "\n":
                            valid = True
                            break
                    except IndexError:
                        pass
            if valid:
                sum += int(number)       
            end_col += step
            
print(sum)



