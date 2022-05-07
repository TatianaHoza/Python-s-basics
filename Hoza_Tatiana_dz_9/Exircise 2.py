class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, m=25, l=5):
        print(f'Масса асфальта:{self._length * self._width * m * l /1000} тонн')

Road = Road(20, 5000)
Road.mass()