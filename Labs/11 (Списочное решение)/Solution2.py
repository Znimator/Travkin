# Дан спиисок натуральных чисел, найти среди них простые.
from random import randint

def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

nums = [randint(1,100) for _ in range(1, 100)]

print(nums)
matches = [x for x in nums if IsPrime(x)]
print(matches)