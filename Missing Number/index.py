def missingNumber(nums):
    n = len(nums)

    total_sum = sum(nums)
    expected_sum = (n*(n+1))//2
    missing_number = expected_sum - total_sum

    return missing_number

nums1 = [3,0,1]
nums2 = [0,1]
nums3 = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums3))