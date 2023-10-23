import math

a,b,c = 0,0,0
pick = int(input("method: "))

if pick == 1:
    x = int(input("x:"))
    y = int(input("y:"))
elif pick == 2:
    x = float(input("x:"))
    y = float(input("y:"))

a = (1 + y) * ((x + y ** 2)/ math.exp(-x-2)) + (1/y)
b = 1 + abs(y-x) + ( (y - x)**2 / 2) + ((abs(y-x) ** 3) / (x * (y - 10)))
c = ((x + 10 + y) ** 2) * ((math.sin(x) + math.sin(x+5) ** 2) / abs(x - y - 5))

print("a:", a)
print("b:", b)
print("c:", c)