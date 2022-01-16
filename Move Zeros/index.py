def moveZeros(arr):
    n = len(arr)
    num_counts = 0
    for num in arr:
        if num != 0:
            arr[num_counts] = num
            num_counts+=1
    for i in range(num_counts,n):
        arr[i] = 0
    return arr


arr = [0, 1, 3, 0, 12]
arr1 = [0,1,2,3,4,6,7]
print(moveZeros(arr1))