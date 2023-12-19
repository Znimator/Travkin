# Дана квадратная матрица А(N,N) натуральных чисел. Повернуть ее
# относительно центра симметрии на 270 против часовой стрелки.

import random
num = int(input('n = '))

def createMatrix(n):
    matrix = []
    m = []
    for i in range(n):
        for i in range(n):
            m += [random.randint(1, 100)]
        matrix.append(m)
        m = []
    return matrix

def printOut(matrix):
    for i in matrix:
        print(i, ' ')

def turn(matrix): 
    m = []
    m_ = []
    for j in range(len([*matrix][0])):
        for i in range(len(matrix)):
            m += [matrix[i][j]]
        m_.append(m)
        m = []
    return m_ 

def reverse(matrix):
    for i in (matrix):
        return [i[::-1] for i in matrix]
   
def rotate(matrix):
    return reverse(turn(reverse(turn(reverse(turn(matrix))))))

matrix = createMatrix(num)
printOut(matrix)
print("--------------------")
           
print(printOut(rotate(rotate(rotate(matrix)))))
