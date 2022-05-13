class Data:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def extract(cls, day_month_year):
        my_data = []

        for i in day_month_year.split():
            if i != '-': my_data.append(i)

        return int(my_data[0]), int(my_data[1]), int(my_data[2])

    @staticmethod
    def validation(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Правильно'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Сегодня: {Data.extract(self.day_month_year)}'


a = Data('12 - 05 - 2022')
print(a)
print(a.validation(1, 11, 2022))
print(a.validation(1, 25, 2012))
print(a.validation(40, 11, 2021))