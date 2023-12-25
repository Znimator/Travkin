# Составьте географический словарь.
# В первой строчке записано целое число – количество стран. В
# следующих N строчках записана информация о странах. Каждая строчка
# состоит из названия страны и разделённых пробелом названий городов
# этой страны, перечисленных через запятую.
# В следующей строке записан запрос — это название города. Для
# каждого из запроса выведите название страны, в котором находится
# данный город. Если названия города нет в словаре, оставьте строку
# ответа пустой.

count = int(input("Количество стран: "))
countries = {}

for i in range(count):
    name = input("Название страны: ")
    N = int(input("Количество городов: "))
    towns = set()

    for b in range(N):
        town = input("Название города: ")
        towns.add(town)
    countries[name] = towns

tofind = input("Название города (чтобы вывести страну): ")
for country, town in countries.items():
    if tofind in town:
        print(country)