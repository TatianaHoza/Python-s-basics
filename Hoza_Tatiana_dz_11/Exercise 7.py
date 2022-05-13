class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.n = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма комплексных чисел равна')
        return f'n = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение комплексных чисел равно')
        return f'n = {self.a * other.a - (self.b * other.b)} + {(self.b * other.a + self.a * other.b)} * i'

    def __str__(self):
        return f'n = {self.a} + {self.b} * i'


n_1 = ComplexNumber(1, 2)
n_2 = ComplexNumber(-3, -4)
print(n_1)
print(n_1 + n_2)
print(n_1 * n_2)