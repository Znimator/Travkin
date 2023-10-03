i = int(input("i (>= 1): "))
e = float(input("e (0-1): "))

sum = 0
k = 0
_i = 0

while _i < i:
    x = (v+1) / (v+2)
    if x > e:
        sum += x
        k += 1
    _i += 1

print("sum:", sum * 2)
print("count:", k)