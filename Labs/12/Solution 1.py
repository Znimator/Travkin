def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

def is_fibonacci(number):                                                                                                                                                                      
     a, b = 0, 1                                                                                                                                                                                
     while b < number:                                                                                                                                                                          
         a, b = b, a + b                                                                                                                                                                        
     return b == number                                                                                                                                                          


for i in range(1, 2000):
    if not is_fibonacci(i) and IsPrime(i):
        print(i)