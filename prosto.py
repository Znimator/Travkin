# Заданные числа
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))
d = float(input("Введите число d: "))

# Находим максимумы
max_abcd = max(a, b, c, d)
max_abd = max(a, b, d)
max_acd = max(a, c, d)

# Вывод результатов
print(f"Максимум из a, b, c и d: {max_abcd}")
print(f"Максимум из a, b и d: {max_abd}")
print(f"Максимум из a, c и d: {max_acd}")
