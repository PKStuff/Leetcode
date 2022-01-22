def strStr(haystack, needle):
    try:
        return haystack.index(needle)
    except Exception:
        return -1

haystack = "hello"
needle = "ll"
haystack = ""
needle = ""
print(strStr(haystack, needle))