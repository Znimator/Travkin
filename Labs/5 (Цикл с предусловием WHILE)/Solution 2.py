def F(c):
    return 1.8 * c + 32

a = int(input("a:"))
b = int(input("b:"))

for c in range(a, b, 1):
    print(F(c))

