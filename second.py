n = int(input())
k = 0

while n >= 2**k:
    k += 1 # k = k + 1

print(2**k)

