# Дано целое число K и текстовый файл. Удалить из каждой строки
# файла первые K символов (если длина строки меньше K, то удалить из нее все
# символы).

K = int(input("K: "))
f = open(r"Labs/10 (Работа с файлами в PYTHON)/Files/2.txt", 'r+')

t = f.read()
f.truncate(0)
f.seek(0)
newText = t[K:]
f.write(newText)