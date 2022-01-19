from unittest import result


def groupAnagrams(strs):
    element_map = {}
    for string in strs:
        ascii_count = sum([ord(i) for i in string])
        if ascii_count in element_map:
            element_map[ascii_count].append(string)
        else:
            element_map[ascii_count] = [string]
    
    result = []
    for value in element_map.values():
        result.append(value)
    return result

strs = ["eat","tea","tan","ate","nat","bat"]
strs1 = ["a"]
print(groupAnagrams(strs1))