a = float(input('Введите число а:'))
b = float(input('Введите число b:'))
c = float(input('Введите число c:'))
d = float(input('Введите число d:'))

def F(a, b, c, d):
    if a > b and a > c and a > d:
        return a
    if b > a and b > c and b > d:
        return b
    if c > a and c > b and c > d:
        return c
    else:
        return d
print(F(a, b, c, d))