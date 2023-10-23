# Даны действительные числа a,b,c,d. Получить max (A,B,C), max(A,B,D), max(A,C,D)

def _max(*args):
    m = 0
    for v in args:
        if v > m:
            m = v
    return m

# Заданные числа
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))
d = float(input("Введите число d: "))

# Находим максимумы
max_abcd = _max(a, b, c, d)
max_abd = _max(a, b, d)
max_acd = _max(a, c, d)

# Вывод результатов
print(f"Максимум из a, b, c и d: {max_abcd}")
print(f"Максимум из a, b и d: {max_abd}")
print(f"Максимум из a, c и d: {max_acd}")