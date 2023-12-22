#Дан список натуральных чисел, создайте новый список, в котором каждое число будет возведено в квадрат.
from random import randint

nums = [randint(1,100) for _ in range(1, 100)]

print(nums)
newnums = [x**2 for x in nums]
print(newnums)