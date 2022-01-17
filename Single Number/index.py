def singleNumber(nums):
    return 2*(sum(set(nums))) - sum(nums)


nums1 = [2,2,1]
nums2 = [4,1,2,1,2]
nums3 = [1]
print(singleNumber(nums3))