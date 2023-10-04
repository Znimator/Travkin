i = int(input("i (>= 1): "))
e = float(input("e (0-1): "))

k = 0
sum = 0
c = 0

for v in range(i):
    x = (v+1) / (v+2)
    if x > e:
        sum += x
        k += 1

print("sum:", sum * 2)
print("count :", k)