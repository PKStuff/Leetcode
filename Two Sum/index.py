def twoSum(nums: list, target: int) -> list:
    element_map = {}
    for pos in range(len(nums)):
        element_map[nums[pos]] = pos

    for pos in range(len(nums)):
        remaining = target - nums[pos]
        if remaining in element_map and pos != element_map[remaining]:
            return [pos, element_map[remaining]]

nums = [3,3]
target = 6
print(twoSum(nums, target))
