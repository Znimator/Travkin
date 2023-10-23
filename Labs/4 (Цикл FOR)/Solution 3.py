# Дано натуральное число N. Определить, является ли оно простым.

import math
import random

pick = int(input("Рандом(1) или Самому(2)"))

a = 0

if pick == 1:
    a = random.randint(1, 999)
else:
    a = int(input())
    
print(a)
print(a%2 != 0 and a != 2)
