def f(i, e, v = 0, k = 0, sum = 0, c = 0):
    x = (v+1) / (v+2)
    if x > e:
        sum += x
        k += 1
    if c < i:
        c += 1
        f(i, e, v+1, k, sum, c)
    print(sum)
    return sum