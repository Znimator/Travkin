n = int(input("Введите n:"))
if n==1 or n%10==1:
    print(n,' год')
elif 1<n<5 or 21<n<25 or 31<n<35 or 41<n<45 or 51<n<55 or 61<n<65 or 71<n<75 or 81<n<85 or 91<n<95:
    print(n,' года')
else:
    print(n,' лет')
    
