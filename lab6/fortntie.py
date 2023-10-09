def f(i, e):
    sum = 0
    k = 0
    v = 0

    while v < i:
        x = (v+1) / (v+2)
        if x > e:
            sum += x
            k += 1
        v += 1 
    
    return sum * 2, k