duration = int(input('Введите время в секундах: '))
if duration < 60:
    print(duration, 'сек')
elif duration < 3600:
    time_m = duration // 60
    time_s = duration % 60
    print(time_m, 'мин', time_s, 'сек')
elif duration < 86400:
    time_h = duration // 3600
    time_m = (duration % 3600) // 60
    time_s = duration - (time_h * 3600) - (time_m * 60)
    print(time_h, 'час', time_m, 'мин', time_s, 'сек')
else:
    time_d = duration // 86400
    time_h = (duration % 86400) // 3600
    time_m = ((duration % 86400) % 3600) // 60
    time_s = duration - (time_d * 86400) - (time_h * 3600) - (time_m * 60)
    print(time_d, 'дн', time_h, 'час', time_m, 'мин', time_s, 'сек')
