# Question:
    # Given an array of integers, 
    # return indices of the two numbers such that 
    # they add up to a specific target.

# Restate:
    # Return the index of 2 numbers that 
    # add up to a target determined later

# Clarifying Qs:
    # Can the same number be used twice?

# Assumptions:
    # Each input has one solution
    # can't be used twice

# Thoughts/Solution:
    # need some sort of loop to go throught the array

def sum_of_two(arr, target):
    for num1 in range(len(arr)): # For as long as num1 is in the array
        for num2 in range(num1+1,len(arr)): # For as long as num2 is in the array
            if arr[num1] + arr[num2] == target: # If num1 and num2 in the array equal the target,
                return (num1, num2) # return the index where num1 and num2 are at in the array.
    return None # if there aren't numbers in the array that equal the target, return None 
 
# Create a sample array
numbers = [1, 3, 5, 7, 10]
print(sum_of_two(numbers, 9)) # Should return None
print(sum_of_two(numbers, 8)) # Should return (0, 3)


