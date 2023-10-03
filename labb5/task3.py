N = input("N:")

sum = 0
l = len(N)
_l = 0

while _l < l:
    sum += int(N[_l]) ** l
    _l += 1

if sum == int(N):
    print(True)
else:
    print(False)