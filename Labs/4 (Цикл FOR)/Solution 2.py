import math
import random

pick = int(input("Рандом(1) или Самому(2)"))

N = 0
A = 0

if pick == 1:
    N = random.randint(1, 100)
    A = random.randint(1, 100)
else:
    N = int(input("n:"))
    A = int(input("a:"))

mul = 1

for i in range(1, N+1):
    if i+1 < A < math.factorial(i):
        mul *= A

print(1/mul)