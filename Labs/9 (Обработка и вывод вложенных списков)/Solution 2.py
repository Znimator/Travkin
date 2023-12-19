# По данным числам n и m заполните двумерный массив размером n×m
# числами от 1 до n×m ―диагоналями‖, как показано в примере. Выведите
# полученный массив, отводя на вывод каждого элемента ровно 4 символа.

def fill_diagonals(n, m):
    matrix = [[0] * m for _ in range(n)]
    num = 1

    for d in range(n + m - 1):
        for i in range(max(0, d - m + 1), min(d, n - 1) + 1):
            j = d - i
            matrix[i][j] = num
            num += 1

    for i in range(n):
        for j in range(m):
            print(f'{matrix[i][j]:4}', end='')
        print()

fill_diagonals(4, 4)