# По данным числам n и m заполните двумерный массив размером n×m
# числами от 1 до n×m ―диагоналями‖, как показано в примере. Выведите
# полученный массив, отводя на вывод каждого элемента ровно 4 символа.
from Array2D import array2d

n, m = int(input("n:")), int(input("m: "))

a = array2d(n, m)
