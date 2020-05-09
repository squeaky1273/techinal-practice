# Given two arrays, write a function to compute their intersection.

# good inputs: arr1 = [1,2,3,4] arr2 = [4,5,6,7]; arr1 = [3,4,2,5] arr2 = [5,1,7,8]
# edge cases: arr1 = [1,2,3,4] arr2 = [2,4,5,6]; arr1 = [3,2,6,7] arr2 = [2,5,8,7]
# bad inputs: arr1 = [1,2,3,a] arr2 = [4,5,6,s]; arr1 = [1,D,3,4] arr2 = [4,D,6,7]

# Variable: Value
# arr1 = [1,4,3,2]
# arr2 = [7,5,6,4]
# num = 4

# pseudocode:
# function name:
#     create a new set
    # check if values in array 1
        # add valur to new set
    # check if values in array 2
    #     if values if array 1 and 2
    #     add to the new set
        # return new array

def intersection(arr1, arr2):
    my_set = {}
    for i in arr1:
        if i in my_set:
            my_set[i] += 1
        else:
            my_set[i] = 1
    new_set = []
    for i in arr2:
        if i in my_set and my_set[i]:
            my_set[i] -= 1
            new_set.append(i)
    return new_set

arr1 = [1,5,4,3]
arr2 = [7,5,6,4]

print(intersection(arr1, arr2))