import math
def findSecondSmallNumber(nums):
    if len(nums)<=1:
        return None
    small_number = nums[0]
    second_smallest_number = math.inf
    for i in range(len(nums)):
        if nums[i] < small_number:
            second_smallest_number = small_number
            small_number = nums[i]
        elif nums[i] < second_smallest_number and nums[i]!=small_number:
            second_smallest_number = nums[i]
    return small_number, second_smallest_number
    

nums = [6,1,3,2,5,7,0,2]
print(findSecondSmallNumber(nums))