# Дано число n. Создайте массив размером n×n и заполните его по
# следующему правилу: Числа на диагонали, идущей из правого верхнего в
# левый нижний угол равны 1. Числа, стоящие выше этой диагонали, равны 0.

from Array2D import array2d 

n = int(input("n: "))
k = n - 1

a = array2d(n,n)

print(a)

for i in range(n):
    for b in range(n):
        if b == k:
            a[i][b] = 1
            k -= 1
        else:
            a[i][b] = 0

print(a)