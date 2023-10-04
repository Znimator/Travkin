input_string = input("Введите строку: ")

if len(input_string) % 2 == 0:
    first_char = input_string[0]
    result_string = first_char + input_string[1:].replace(first_char, '')

    print("Результат:", result_string)
else:
    print("Длина строки не является четным числом.")
