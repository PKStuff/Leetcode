def containsDuplicate(nums: list[int]) -> bool:
    # return len(set(nums)) != len(nums)
    element_map = {}
    for num in nums:
        if num in element_map:
            return True
        element_map[num] = True
    return False

nums = [1,2,3,4]
print(containsDuplicate(nums))
