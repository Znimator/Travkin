# Вывести на экран все целые числа в диапазоне от 1 до 2000, которые не
# являются числами Фибоначчи и являются простыми числами. Числа
# Фибоначчи вычисляются по такому правилу: F1 = 1, F2 = 1, ∀ n>2 Fn =
# Fn-1 + Fn-2 (текущий элемент последовательности Фибоначчи равен сум-
# ме двух предыдущих)

def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

def fibonacci_sequence(n):
    sequence = set()
    a, b = 0, 1
    while a <= n:
        sequence.add(a)
        a, b = b, a + b
    return sequence
                                                                                                                                                                                                
fib_sequence = fibonacci_sequence(2000)

for i in range(1, 2000):
    if not (i in fib_sequence) and IsPrime(i):
        print(i)