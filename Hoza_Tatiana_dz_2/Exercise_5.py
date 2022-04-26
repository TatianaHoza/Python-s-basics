my_price = [57.8, 46.51, 97, 100, 66.7, 120, 52.2, 200.1, 99.9, 86.7]
for i in my_price:
    r = int(i)
    kk = (i - int(i)) * 100
    print(f'{r} руб {kk:02.0f} коп', end=',')
print(f'\nСписок цен по возрастанию:{my_price.sort()}') # Возвращает None
print(f'\nСписок цен по возрастанию:{sorted(my_price)}') # Использовала для вывода самого списка
if id(my_price) == id(my_price.sort()):
    print('Объект списка после сортировки остался тот же')
else:
    print(False)
print(f'\nСписок цен по убыванию:{my_price.sort(reverse=True)}') # Возвращает None
my_price = [57.8, 46.51, 97, 100, 66.7, 120, 52.2, 200.1, 99.9, 86.7]
print(f'\nСписок цен по убыванию:{reversed(my_price)}')


