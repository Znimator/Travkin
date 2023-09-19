import math
h = float(input("Hours: "))
m = float(input("Minutes: ")) 
s = float(input("Seconds: "))

MaxTime = 43200
totalSeconds = (h * 60 * 60) + (m * 60) + (s)
if totalSeconds > MaxTime:
    totalSeconds -= MaxTime * math.floor(totalSeconds/MaxTime)


print(360 * totalSeconds/MaxTime)