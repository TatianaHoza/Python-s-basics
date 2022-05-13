class StopError(Exception):
    def __init__(self, text):
        self.text = text

my_list = []
while True:
    a = input('введите список:').split()
    try:
        for i in a:
            if i in '1234567890':
                my_list.append(a)
            elif i == 'stop':
                break
            else:
                raise StopError('Error')
    except StopError as err:
        print('вы ввели не число!', err)