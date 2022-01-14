def isBadVersion(version):
    if version > 4:
        return 1
    return 0

def firstBadVersionIterative(n):
    for version in range(1, n+1):
        if isBadVersion(version):
            return version
    return -1

def firstBadVersion(n):
    left = 1; right = n
    while left <= right:
        mid = (left+right)//2
        bad_version = isBadVersion(mid)
        if bad_version:
            if isBadVersion(mid-1):
                right = mid-1
            else:
                return mid
        else:
            left = mid + 1
    return -1

# inputs
n = 5
print(firstBadVersionIterative(n))
print(firstBadVersion(n))
