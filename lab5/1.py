i = int(input("i (>= 1): "))
e = float(input("e (0-1): "))

k = 0
sum = 0
c = 0

def f(v):
    global k
    global sum
    global c
    
    x = (v+1) / (v+2)
    print(x)
    print(e)
    if x > e:
        sum += x
        k += 1
    if c < i:
        c += 1
        f(v+1)


#for v in range(i):
#    x = (v+1) / (v+2)
#    if x > e:
#        sum += x
#        k += 1

f(i)

print("sum:", sum * 2)
print("count :", k)