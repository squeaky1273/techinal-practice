def find_if_duplicates(arr):
    for num1 in range(len(arr)):
        for num2 in range(0, num1):
            if arr[num1] == arr[num2]:
                return True
    return False

arr = [10, 3, 4, 2, 2, 6]
if find_if_duplicates(arr):
    print("There are duplicates")
else:
	print("No duplicates")