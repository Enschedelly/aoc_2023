sum = 0

with open('inputs/calibration_document.txt') as cd:
    for line in cd:
        digits = []
        number = ""
        for char in line:  # loop through all chars to check if they are a digit. 
            if char.isdigit():
                digits.append(char)   # If so, append them to the digits array.
        number += digits[0]  # Then take the first and last element out of that array.
        number += digits[-1]
        sum += int(number)  # And add this calibration value to the sum of all values.

print(sum)