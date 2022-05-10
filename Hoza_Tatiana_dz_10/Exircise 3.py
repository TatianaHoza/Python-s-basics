class Cell:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return f'Число ячеек - {self.n}'

    def __add__(self, other):
        return Cell(self.n + other.n)

    def __sub__(self, other):
        return Cell(self.n - other.n) if self.n - other.n > 0 \
           else "Разность количества ячеек менее нуля!"

    def __mul__(self, other):
        return Cell(self.n * other.n)

    def __truediv__(self, other):
        return Cell(self.n // other.n)

    def make_order(self, count):
        x = self.n
        while x > 0:
            for i in range(1, count+1):
                print('*', end=' ')
                x -= 1
                if x <= 0:
                    break
            print('\n', end='')



n_1 = Cell(12)
n_2 = Cell(5)
print(n_1 + n_2)
print(n_1 - n_2)
print(n_1 * n_2)
print(n_1 / n_2)
print(n_2.make_order(2))