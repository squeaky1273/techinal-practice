def find_if_duplicates(arr, n):
    new_set = []
    for i in range(n):
        if arr[i] in new_set:
                return True
                new_set.append(arr[i])
        return False

arr = [10, 3, 4, 2, 2, 6]
n = len(arr)
if find_if_duplicates(arr, n):
    print(“There are duplicates”)
else:
	print(“No duplicates”)