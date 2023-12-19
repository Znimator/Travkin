# Дана квадратная матрица А(N,N) натуральных чисел. Повернуть ее
# относительно центра симметрии на 270 против часовой стрелки.

from Array2D import array2d
from random import randint


N = int(input("N: "))
a = array2d(N,N)
for n in a:
    for i in range(len(n)):
        n[i] = randint(0, 1000)
    print(n)

for i in range(3):
    a = rotate90(a)
print("------------------------------------")
print(a)