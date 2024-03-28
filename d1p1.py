sum = 0

with open('inputs/calibration_document.txt') as cd:
    for line in cd:
        digits = []
        number = ""
        for char in line:
            if char.isdigit():
                digits.append(char)
        number += digits[0]
        number += digits[-1]
        sum += int(number)

print(sum)