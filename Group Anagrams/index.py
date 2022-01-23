def groupAnagrams(strs):
    element_map = {}
    for string in strs:
        sorted_string = ''.join(sorted(string))
        if sorted_string in element_map:
            element_map[sorted_string].append(string)
        else:
<<<<<<< HEAD
            element_map[ascii_count] = [string]

=======
            element_map[sorted_string] = [string]
    
>>>>>>> fe8676fcbdee8ea4d12a73f08b4d6353906eefbe
    result = []
    for value in element_map.values():
        result.append(value)
    return result

strs = ["eat","tea","tan","ate","nat","bat"]
strs1 = ["a"]
<<<<<<< HEAD
strs2 = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
print(groupAnagrams(strs2))
=======
print(groupAnagrams(strs))
>>>>>>> fe8676fcbdee8ea4d12a73f08b4d6353906eefbe
