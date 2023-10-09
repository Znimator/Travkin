input_string = input("Введите строку: ")

# Проверяем, что длина строки четная
if len(input_string) % 2 == 0:
    first_char = input_string[0] # Получаем первый символ
    modified_string = first_char # Начинаем с первого символа

# Проходим по остальным символам строки и добавляем их в измененную строку,
# только если они не равны первому символу
    for char in input_string[1:]:
        if char != first_char:
            modified_string += char

    print("Измененная строка:", modified_string)
else:
    print("Длина строки нечетная, не требуется удаление.")