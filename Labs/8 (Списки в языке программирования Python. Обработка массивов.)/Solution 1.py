# Дан массив натуральных чисел А(N), значения элементов которого
# лежат в диапазоне [150,2000]. Найти: а) сумму элементов массива, которые
# являются четными и имеют два нуля в своей записи б) максимальный элемент
# среди тех, которые не являются простыми

def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

print(IsPrime(3))

choice = int(input("Рандом (1) или Ручной ввод (2):"))

arr = []
_sum = 0
mElement = 0

if choice == 1:
    from random import randint
    N = 10
    for i in range(N):
        arr.append(randint(150, 2000))
    print(arr)
elif choice == 2:
    print("Вводите числа, для завершения напишите '-1'")
    while True:
        x = int(input())
        if x == -1:
            break
        elif x < 150 or x > 2000:
            print("(!) Вне диапазонна [150 : 2000]")
        else:
            arr.append(x)


for i in arr:
    print(str(i).count("0"))
    if i % 2 == 0 and str(i).count("0") == 2:
        _sum += i

for i in arr:
    if not(IsPrime(i)) and i > mElement:
        mElement = i

print(arr)
print(_sum, mElement)