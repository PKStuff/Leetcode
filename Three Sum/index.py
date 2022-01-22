def threeSum(nums):
    result = []
    n = len(nums)
    target = 0
    if n < 3:
        return []

    nums = sorted(nums)
    for i in range(len(nums)):
        left = i+1
        right = len(nums)-1
        while left < right:
            current_sum = nums[left]+nums[right]+nums[i]
            if current_sum < target:
                left+=1
            elif current_sum > target:
                right-=1
            else:
                if [nums[i], nums[left], nums[right]] not in result:
                    result.append([nums[i], nums[left], nums[right]])
                left+=1
                right-=1
    
    return result




nums = [-1,0,1,2,-1,-4]
nums = [0,0,0,0]
# nums = [-2,0,1,1,2]
print(threeSum(nums))
