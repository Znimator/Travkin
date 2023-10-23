# /Images/Task 3.png

i = int(input("i (>= 1): "))
e = float(input("e (0-1): "))

sum = 0
k = 0
v = 0

while v < i:
    x = (v+1) / (v+2)
    if x > e:
        sum += x
        k += 1
    v += 1

print("sum:", sum * 2)
print("count:", k)