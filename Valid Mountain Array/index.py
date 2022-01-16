def validMountainArray(arr):
    if len(arr) < 3:
        return False
    i = 1
    n = len(arr)
    while i < n and arr[i] > arr[i-1]:
        i+=1
    if i == 1 or i == n:
        return False
    while i < n and arr[i] < arr[i-1]:
        i+=1
    return i==n


arr1 = [3, 5, 5]
arr2 = [0, 3, 2, 1]
arr3 = [1,2,3,4,5,4]
print(validMountainArray(arr3))
