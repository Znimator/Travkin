# Images/Task4.png

# Натуральные числа и найти отрицательные?!?!?

def find_max_negative(matrix, S, P):
    K = len(matrix)
    max_negative = float('-inf')

    # Найти индексы элемента B(S, P)
    i, j = S, P

    # Определить границы области
    start_row, end_row = min(i, j), max(i, j)
    start_col, end_col = max(0, j - i), min(K, j + (K - i))

    # Найти максимальное отрицательное значение внутри области
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col):
            if row != i or col != j:  # Исключаем элемент B(S, P)
                current_value = matrix[row][col]
                if current_value < 0 and current_value > max_negative:
                    max_negative = current_value

    return max_negative

# Пример использования функции
matrix = [
    [1, 2, -3, 4],
    [5, 6, 7, -8],
    [9, -10, 3, -12],
    [13, 14, 15, 16]
]

S, P = 2, 2  # Пример координат элемента B(S, P)

result = find_max_negative(matrix, S, P)

if result == float('-inf'):
    print("В указанной области нет отрицательных элементов.")
else:
    print(f"Максимальный отрицательный элемент в области: {result}")