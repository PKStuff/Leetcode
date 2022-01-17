import math
def countPrimes(n):
    if n < 2:
        return 0
    isprime = [True]*n
    isprime[0] = isprime[1] = False
    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if isprime[i]:
            for mul_num in range(i*i, n, i):
                isprime[mul_num] = False
    return sum(isprime)


n = 10
print(countPrimes(n))