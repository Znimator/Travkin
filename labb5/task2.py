N = input("N:")

sum = 0
l = len(N)

for n in range(l):
    sum += int(N[n]) ** l

if sum == int(N):
    print(True)
else:
    print(False)



print("hello")