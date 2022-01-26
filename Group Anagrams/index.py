def groupAnagrams(strs):
    element_map = {}
    for string in strs:
        sorted_string = ''.join(sorted(string))
        if sorted_string in element_map:
            element_map[sorted_string].append(string)
        else:
            element_map[sorted_string] = [string]
    result = []
    for value in element_map.values():
        result.append(value)
    return result

strs = ["eat","tea","tan","ate","nat","bat"]
strs1 = ["a"]
strs2 = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
print(groupAnagrams(strs2))
print(groupAnagrams(strs))
