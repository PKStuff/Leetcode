def searchRangeIterative(nums, target):
    if len(nums) == 0:
        return [-1, -1]
    left_ptr = -1
    right_ptr = -1
    for left in range(len(nums)):
        if nums[left] == target:
            left_ptr = left
            break
        if nums[left] > target:
            break

    for right in range(len(nums)-1, -1, -1):
        # print(right)
        if nums[right] == target:
            right_ptr = right
            break
        if nums[right] < target:
            break
    return [left_ptr, right_ptr]

def searchRange(nums, target):
    if len(nums) == 0:
        return [-1, -1]
    left_index = -1
    right_index = -1

    # search left side first
    left = 0; right = len(nums)-1
    while left <= right:
        mid = (left + right)//2
        if nums[mid] == target:
            if mid == 0 or nums[mid-1] != target:
                left_index = mid
                break
            right = mid-1
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1

    # search right side
    left = 0; right = len(nums)-1
    while left <= right:
        mid = (left + right)//2
        if nums[mid] == target:
            if mid == len(nums)-1 or nums[mid+1] != target:
                right_index = mid
                break
            right = mid-1
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1

    return [left_index, right_index]


num1 = [5, 7, 7, 8, 8, 10]
target1 = 5
output1 = [3,4]
num2 = [5, 7, 7, 8, 8, 10]
target2 = 6
output2 = [-1,-1]
num3 = []
target3 = 0
output3 = [-1,-1]
print(searchRangeIterative(num1, target1))
print(searchRange(num1, target1))
