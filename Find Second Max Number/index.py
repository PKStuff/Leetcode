def secondMaxNumber(nums):
    first_num = 0
    for num in nums:
        if num > first_num:
            first_num = num
    
    second_num = 0
    for num in nums:
        if num > second_num and num!=first_num:
            second_num = num
    return second_num

def secondMaxNumberOptimized(nums):
    first_num = 0
    second_num = 0
    for num in nums:
        if num > first_num:
            second_num = first_num
            first_num = num
        elif num > second_num and num != first_num:
            second_num = num
    return second_num


nums = [32, 64, 64, 12, 45, 34, 35, 12]
print(secondMaxNumber(nums))
print(secondMaxNumberOptimized(nums))