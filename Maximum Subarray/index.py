import math
def maxSubArray(nums):
    sum = 0
    max_sum = -math.inf
    for i in range(len(nums)):
        sum+=nums[i]
        if sum > max_sum:
            max_sum = sum
        if sum < 0:
            sum = 0
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [5,4,-1,7,8]
# nums = [-1]
print(maxSubArray(nums))