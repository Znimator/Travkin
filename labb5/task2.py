a = int(input("Введите начальную температуру в градусах Цельсия (C): "))
b = int(input("Введите конечную температуру в градусах Цельсия (C): "))

print("Таблица перевода температуры из C в F:")
print("Celsius (C)\tFahrenheit (F)")

while a <= b:
    fahrenheit = 1.8 * a + 32
    a += 1
print(f"{a}\t\t{fahrenheit}")





