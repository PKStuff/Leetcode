import math
def maxSumBruteForce(arr, k):
    max_sum = -math.inf
    n = len(arr)
    for i in range(n-k+1):
        sum = 0
        for j in range(i, i+k):
            sum+=arr[j]
        max_sum = max(max_sum, sum)
    return max_sum


def maxSum(arr, k):
    n = len(arr)
    window_sum = sum(arr[i] for i in range(0,k))
    max_sum = window_sum

    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(max_sum, window_sum)
    return max_sum
arr = [80, -50, 90, 100]
k = 2
print(maxSumBruteForce(arr, k))
print(maxSum(arr, k))