import math
x = float(input("X: "))
a = float(input("A: "))


if x > a:
    print(x * (x - a) ** 0.5)
elif x == a:
    print(x / math.sin(a * x))
elif x < a:
    print(math.exp(-a * x) * math.cos(a * x))