def searchInsert(nums: list, target:int):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        if target > nums[mid]:
            left = mid+1
        else:
            right = mid-1
    return left if left!=right else left+1

nums = [1,3,5,7]
target = 9
print(searchInsert(nums, target))