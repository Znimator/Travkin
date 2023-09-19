import math

N = int(input("n:"))
A = int(input("a:"))

mul = 1

for i in range(1, N+1):
    if i+1 < A < math.factorial(i):
        mul *= A

print(1/mul)