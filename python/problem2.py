# Question:
    # Given an array of integers, find if the array contains any duplicates.

# Restate:
    # Indicate if a given arrray have duplicate integers

# Clarifying Qs:
    # How should I indicate whethter duplicates exist?

# Assumptions:
    # If there are duplicates, return True
    # If there aren't duplicates, return False

# Thoughts/Solution:

def find_if_duplicate(arr):
    for num1 in range(len(arr)): # For as long as num1 is in the array
        for num2 in range(0, num1): # For as long as num2 is in the array
            if arr[num1] == arr[num2]: # If 2 integers are equal to each other, 
                return True # Return True (there is a duplicate)
    return False # else return False (no duplcates)

# Create sample array
arr = [1, 2, 3, 4, 5]
print(find_if_duplicate(arr)) # Should return False (no duplicates)

arr = [1, 2, 3, 4, 4, 5]
print(find_if_duplicate(arr)) # Should return True (duplicates exist)