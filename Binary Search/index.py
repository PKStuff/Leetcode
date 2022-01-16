def binary_search(arr, key):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# Driver Code
arr  = [1, 2, 3, 4, 5]
print(binary_search(arr, -1))

# Time Complexity: O(n)