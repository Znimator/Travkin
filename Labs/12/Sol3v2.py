# Составьте географический словарь.
# В первой строчке записано целое число – количество стран. В
# следующих N строчках записана информация о странах. Каждая строчка
# состоит из названия страны и разделённых пробелом названий городов
# этой страны, перечисленных через запятую.
# В следующей строке записан запрос — это название города. Для
# каждого из запроса выведите название страны, в котором находится
# данный город. Если названия города нет в словаре, оставьте строку
# ответа пустой.

import re

count = int(input("Количество стран: "))
countries = {}

for i in range(count):
    info = input("Название страны и города через запятую: ")
    towns = set()
    
    words = re.findall(r"\w+", info)

    countries[words[0]] = words[1:]

tofind = input("Название города (чтобы вывести страну): ")
for country, towns in countries.items():
    if tofind in towns:
        print(country)