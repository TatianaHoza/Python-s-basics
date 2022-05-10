from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, a):
        self.a = a

    @abstractmethod
    def expense(self):
        pass

    def __str__(self):
        return str(self.a)


class Coat(Clothes):

    @property
    def expense(self):
        return self.a / 6.5 + 0.5


class Suit(Clothes):

    @property
    def expense(self):
        return self.a * 2 + 0.3


V = Coat(44)
H = Suit(1.64)
print(f' Расход ткани для пошива пальто {V} размера - {round(V.expense)}')
print(f' Расход ткани для пошива костюма на рост {H} м - {round(H.expense)}')