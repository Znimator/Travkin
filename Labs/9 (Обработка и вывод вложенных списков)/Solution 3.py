# Дана матрица B(N,M) натуральных чисел. Найти количество строк, в
# которых меньше половины элементов начинается с заданной цифры Х.

from Array2D import array2d
from random import randint
from math import floor


a = array2d(int(input("N: ")), int(input("M: ")))

for n in a:
    for i in range(len(n)):
        n[i] = randint(0, 100000)

x = input("X: ")

count = 0

for n in a:
    print(n)
    k = 0
    for i in n:
        if str(i)[0] == x:
            k += 1
    if 0 < k <= floor(len(n) / 2):
        count += 1

print(f"Count: {count}")