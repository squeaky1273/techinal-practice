# Prompt: 
# Given an array nums containing n + 1 
# integers where each integer is between 1 
# and n (inclusive), prove that at least one 
# duplicate number must exist. Assume that there 
# is only one duplicate number, find the duplicate one.

# Restate: Find the duplicate in the array

# Clarifying Qs: Are the arrays expected to be sorted?

# Assumptions: There is at least one duplicate

# Thoughts/Solution:

# good inputs: arr = [1, 2, 3, 3]; arr = [1, 3, 3, 5]
# edge cases: arr = [2, 1, 2, 4]; arr = [3, 4, 1, 4]
# bad inputs: arr = [1, 2, 3, 4]; arr = [5, 6, 7, 8]

# variable table:
# arr : [1, 2, 3, 3]
# i : 1, 2, 3

# psuedocode:

# time complexity: O(n)
# space complexity: O(n)

def find_duplicate_in_array(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            return arr[i]

# Good inputs
arr = [1, 2, 3, 3]
print(find_duplicate_in_array(arr))

arr = [1, 3, 3, 5]
print(find_duplicate_in_array(arr))

# Edge cases
arr = [2, 1, 2, 4]
print(find_duplicate_in_array(arr))

arr = [2, 1, 2, 4]
print(find_duplicate_in_array(arr))

# Bad inputs
arr = [1, 2, 3, 4]
print(find_duplicate_in_array(arr))

arr = [5, 6, 7, 8]
print(find_duplicate_in_array(arr))