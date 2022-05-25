class Class(Exception):
    def __init__(self, text):
        self.text = text

a = int(input('введите число а:'))
b = int(input('введите число b:'))

try:
    if b != 0:
        c = a / b
        print(f'Результат деления: {c}')
    else:
        raise Class('Error')
except Class as err:
    print('Деление на ноль невозможно', err)