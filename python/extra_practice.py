# Given: arr, and int d 
#=> new_arr with d left rotations 

#[1,2,3,4,5], 2 #=> [3,4,5,1,2]
#[5,-2,0,3], 6 #=> [0,3,5,-2] 
# (only need remainder of left rotations) 

# describe a solution(s)
# Pick a solution
# pseudocode solution (Committed to one solution)


# OK to ask the interviewer for syntax if stuck on syntax issues, or just use psuedocode 


# def left_rotation(arr, d):
#     # Shift value over by d
#     for i in range(0, d):
#         # starting value in array
#         start = arr[0]
#         # Shift value over by 1
#         for i in range(len(arr)):
#             if i < len(arr)-1:
#                 arr[i] = arr[i+1]
#         # starting value moved to end of array
#         arr[-1] = start
#     # return shifted array
#     return arr[i]

# arr = [1, 2, 3, 4]
# d = 2

# # variable table
# # arr = [1, 2, 3, 4]
# # d = 2
# # i = 1
# # arr = [3, 4, 1, 2] (after shift)

# using modulos and adding to a new array:
def left_rotate(arr, n, d): 
    new_arr = []
    # Starting point
    mod = d % n 
    for i in range(n): 
        new_arr.append(arr[(mod + i) % n])
    return new_arr

# variable table:
# arr = [1, 2, 3, 4]
# i = 1, 2, 3, 4
# n (length of array) = 4
# d (number of rotations) = 3
# new_arr = [4, 1, 2, 3]


arr = [1, 2, 3, 4]
n = len(arr)
d = 3

print(left_rotate(arr, n, d))





# problem: Find the left rotation, based d number of times it will be moved:


# Assume: function has to be flexible
# Move the left

# Clarifying Qs:
# n/a

# psuedocode:

# function (arr, d)
# create array
# For loop on values in array
    # focus on the index
    # move to the left d times

# return array

# arr = [1, 2, 3, 4]
# d = 2
# new_arr = [3, 4, 1, 2]

# d = 4
# new_arr = [1, 2, 3, 4]

# d = 6
# new_arr = [3, 4, 1, 2]

# def left_rotation(arr, d):
#     new_arr = []
#     for i in arr:
#         # change indx to index - d
#         new_arr.append[i]
#     return new_arr.join(' ')


# variable table
# arr = [1, 2, 3, 4]
# d = 2
# i = 1
# new_arr = [-1, ]

# really good: set up: Qs, assumptions, psudeocode, syntax
# work on: 
# technical knowledge, 
# get to test inputs, think of complexity, come up with own test inputs, 
# abbreviate as much as possible (Given, #=> "return", arr, str, n, int)
