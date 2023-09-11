h = float(input("Hours: "))
m = float(input("Minutes: ")) 
s = float(input("Seconds: "))

MaxTime = 43200
totalSeconds = (h * 60 * 60) + (m * 60) + (s)

print(360 * totalSeconds/MaxTime)