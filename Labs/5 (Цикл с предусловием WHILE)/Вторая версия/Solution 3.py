# /Images/Task 3.png

e = float(input("e (0-1): "))

sum = 0
k = 0
i = 1

while True:
    x = (i + 1) / (i ** 2)
    print(x)

    if x > e:
        sum += x
        k += 1
    else:
        break
    
    i += 1
    

print("sum:", sum * 2)
print("count:", k)