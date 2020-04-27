# Given an integer, write a function to determine if it is a power of four.

# good inputs: num = 16; num = 64
# edge cases: num = 1; num = 4
# bad inputs: num = 'four'; num = 'sixteen'

# pseudocode:
# function name:
    # check if input is 0:
    #     return False
    # while loop: if input is not 1 or 0:
    #     if the input modulus of 4 is not 0:
    #         return False
    #     the num is equal to the input division to 4
    # return True

# Variable: Value
# num = 16

def PowerOfFour(num): 
    if (num == 0): 
        return False
    while (num != 1): 
            if (num % 4 != 0): 
                return False
            num = num // 4
    return True

# good inputs:
if (PowerOfFour(16)):
    print("True")
else:
    print("False")

if (PowerOfFour(64)):
    print("True")
else:
    print("False")

# edge cases:
if (PowerOfFour(4)):
    print("True")
else:
    print("False")

if (PowerOfFour(1)):
    print("True")
else:
    print("False")

# bad inputs:
if (PowerOfFour('sixteen')):
    print("True")
else:
    print("False")

if (PowerOfFour('four')):
    print("True")
else:
    print("False")