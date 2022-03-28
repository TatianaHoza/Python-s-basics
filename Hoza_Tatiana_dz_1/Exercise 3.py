num = int(input('Введите число от 1 до  100: '))
if (num >= 1) and (num <= 100):
    if (num >= 11) and (num <= 14):
        print(num, 'процентов')
    elif num == 1 or str(num)[-1] == '1':
        print(num, 'процент')
    elif str(num)[-1] == '2' or str(num)[-1] == '3' or str(num)[-1] == '4':
        print(num, 'процента')
    elif str(num)[-1] == '5' or str(num)[-1] == '6' or str(num)[-1] == '7' or str(num)[-1] == '8' \
            or str(num)[-1] == '9' or str(num)[-1] == '0':
        print(num, 'процентов')
else:
    print('Вы ввели неверное число. Введите число от 1 до 100!')