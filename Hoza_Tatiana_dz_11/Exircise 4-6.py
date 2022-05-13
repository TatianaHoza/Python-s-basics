class OfficeEquipment:
    def __init__(self):
        self.my_list = []

    def __add__(self, other):
        self.my_list.append(other)

class Equipment:
    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price
        self.group = self.__class__.__name__

    def __repr__(self):
        print(f' {self.name} - {self.year} - {self.price}')


class Printer(Equipment):
    def __init__(self, series, name, year, price):
        super().__init__(name, year, price)
        self.series = series

    def __repr__(self):
        print(f'Принтеры: {self.name} - серии:{self.series} - года выпуска:{self.year} - стоимость: {self.price}')


class Scaner(Equipment):
    def __init__(self, series, name, year, price):
        super().__init__(name, year, price)
        self.series = series

    def __repr__(self):
        print(f'Сканеры: {self.name} - серии:{self.series} - года выпуска:{self.year} - стоимость: {self.price}')


class Xerox(Equipment):
    def __init__(self, series, name, year, price):
        super().__init__(name, year, price)
        self.series = series

    def __repr__(self):
        print(f'Ксероксы: {self.name} - серии:{self.series} - года выпуска:{self.year} - стоимость: {self.price}')

OfficeEquipment = OfficeEquipment()
scaner = Scaner('10', 'Kodak Alaris', '2019', '1200')
OfficeEquipment.__add__(scaner)
scaner = Scaner('9', 'Artec 3D', '2020', '1500')
OfficeEquipment.__add__(scaner)
printer = Printer('15', 'HP Laser 107a', '2016', '800')
OfficeEquipment.__add__(printer)
print(OfficeEquipment.my_list)
print(OfficeEquipment.my_list)