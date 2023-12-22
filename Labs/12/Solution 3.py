f = open(r"Labs/12/countries.txt", encoding='utf-8')

town = input("Город: ")
for i in f.readlines()[1:]:
    if town in i:
        print(i.split()[0])