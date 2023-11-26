def f(e):
    sum = 0
    k = 0
    i = 1

    while True:
        x = (i+1) / (i+2)
        
        if x > e:
            sum += x
            k += 1
        else:
            break

        i += 1
    
    return sum * 2, k