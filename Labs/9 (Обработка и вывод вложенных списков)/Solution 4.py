# Images/Task4.png
from Array2D import array2d
from random import randint
import time

K = 20
matrix = array2d(K, K)
diag = [i for i in range(K)]

for n in matrix:
    for i in range(len(n)):
        n[i] = randint(1, 100)

S, P = 15,3 # X, Y ось

position = matrix[S][P]

for i in matrix:
        print(i, ' ')

k = 0
for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        if x == k:
            diag[y] = x
            matrix[y][x] = 0
            k += 1
            break 

for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        if (y <= P and P < K/2) or (y >= P and P > K/2):
             matrix[y][x] = 0
        if (x >= S and P < K/2) or (x <= S and P > K/2):
             matrix[y][x] = 0 #74-67-27 6 Поликлиника
        if (x <= diag[y] and P < K/2) or (x >= diag[y] and P > K/2):
             matrix[y][x] = 0

m = 0
for i in matrix:
    for num in i:
        if num > m:
            m = num
for i in matrix:
        print(i, ' ')
print(m)