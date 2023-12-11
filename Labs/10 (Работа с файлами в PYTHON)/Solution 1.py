# Дана строка S и текстовый файл. Добавить строку S в конец файла.

f = open(r"Labs/10 (Работа с файлами в PYTHON)/Files/1.txt", "a")
f.write(input("String: "))
f.close()
