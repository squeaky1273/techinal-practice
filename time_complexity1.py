# Prompt: Given an integer, write a function to determine if it is a power of three.

# Restate: Write a function that tells whether the input is a power of 3

# Clarifying Qs:n/a

# Assumptions: Integers are to only be considered

# Thoughts/Solution:

# good inputs: num = 9; num = 81
# edge cases: num = 1; num = 3
# bad inputs: num = 'three'; num = 'nine'

# Variable: Value
# num = 9

# pseudocode:
# function name:
    # check if input is 0:
    #     return False
    # while loop: if input is not 1 or 0:
    #     if the input modulus of 3 is not 0:
    #         return False
    #     the num is equal to the input division to 3
    # return True

# time complexity: O(n)
# space complexity: O(n)

def PowerOfThree(num): 
    if (num == 0): 
        return False
    while (num != 1): 
            if (num % 3 != 0): 
                return False
            num = num // 3
    return True

# good inputs:
if (PowerOfThree(9)):
    print("True")
else:
    print("False")

if (PowerOfThree(81)):
    print("True")
else:
    print("False")

# edge cases:
if (PowerOfThree(3)):
    print("True")
else:
    print("False")

if (PowerOfThree(1)):
    print("True")
else:
    print("False")

# bad inputs:
if (PowerOfThree('nine')):
    print("True")
else:
    print("False")

if (PowerOfThree('three')):
    print("True")
else:
    print("False")
