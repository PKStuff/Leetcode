def majorityElement(nums):
    majority_criteria = len(nums)/2
    element_map = {}
    for element in nums:
        if element in element_map:
            element_map[element]+=1
        else:
            element_map[element]=1
        if element_map[element] > majority_criteria:
                return element

nums = [3,2,3]
nums1 = [2,2,1,1,1,2,2]
print(majorityElement(nums))