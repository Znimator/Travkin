import math
sum = 0
N = int(input())
sinus = 0
for n in range(1, N + 1):
    sinus += math.sin(n)
    sum += (n + 1)/sinus
print(sum)
