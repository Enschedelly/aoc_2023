# checks if an index continues with a number. 
# returns the number if so, else returns 0.
def check_number_exists(line, idx):
    if line[idx:idx+3] == 'one':
        return '1'
    elif line[idx:idx+3] == 'two':
        return '2'
    elif line[idx:idx+5] == 'three':
        return '3'
    elif line[idx:idx+4] == 'four':
        return '4'
    elif line[idx:idx+4] == 'five':
        return '5'
    elif line[idx:idx+3] == 'six':
        return '6'
    elif line[idx:idx+5] == 'seven':
        return '7'
    elif line[idx:idx+5] == 'eight':
        return '8'
    elif line[idx:idx+4] == 'nine':
        return '9'
    else:
        return '0'


sum = 0
with open('inputs/calibration_document.txt') as cd:
    for line in cd:
        digits = []
        for idx in range(len(line)):
            if line[idx].isdigit():
                digits.append(line[idx])
            elif line[idx] in 'otfsen':  # one, two, three, four, five, six, seven, eight, nine
                number = check_number_exists(line, idx)
                if number != '0':
                    digits.append(number)     
        number = digits[0]
        number += digits[-1]
        sum += int(number)

print(sum)              
