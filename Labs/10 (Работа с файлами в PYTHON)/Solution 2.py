# Дано целое число K и текстовый файл. Удалить из каждой строки
# файла первые K символов (если длина строки меньше K, то удалить из нее все
# символы).

K = int(input("K: "))
f = open(r"Labs/10 (Работа с файлами в PYTHON)/Files/2.txt", 'r+')

t = f.readlines()
new = t.copy()

for i in range(len(t)):
    newText = t[i][K:]
    new[i] = newText
    f.truncate(0)
    f.seek(0)
    f.writelines(new)
f.close()