duration = int(input('Введите промежуток времени в секундах '))
day = duration // 86400
hour = (duration % 86400) // 3600
minute = ((duration % 86400) % 3600)// 60
second = ((duration % 86400) % 3600) % 60
if day ==0 and hour == 0 and minute == 0:
    print('duration = ', duration)
    print(second, 'сек')
elif day ==0 and hour == 0:
    print('duration = ', duration)
    print(minute, 'мин', second, 'сек')
elif day ==0:
    print('duration = ', duration)
    print(hour, 'час', minute, 'мин', second, 'сек')
else:
    print('duration = ', duration)
    print(day, 'дн', hour, 'час', minute, 'мин', second, 'сек')




