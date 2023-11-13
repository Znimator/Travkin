# Дана последовательность символов (строка). Если в строке четное
# количество символов, то удалить из нее все вхождения первого символа, кроме
# его самого

input_string = input("Введите строку: ")

if len(input_string) % 2 != 0:
    print("Длинна строки не четная")
    exit()

first_char = input_string[0]

new_string = first_char
for i in input_string:
    if i != first_char:
        print(i)
        new_string += i

print("Результат:", new_string)