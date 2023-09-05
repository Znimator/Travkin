h,m,s = float(input("Hours: ")), float(input("Minutes: ")), float(input("Seconds: "))

MaxTime = 43200
totalSeconds = (h * 60 * 60) + (m * 60) + (s)

#Всего секунд может быть 43200,
#Переводим заданное число в секунды
#находим процент используя totalSeconds/MaxTime
#далее 360 градусов умножаем на тот же самый процент

print(360 * totalSeconds/MaxTime)
