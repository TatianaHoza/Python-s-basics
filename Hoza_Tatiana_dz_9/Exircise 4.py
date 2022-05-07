class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name}  повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость town car {self.name} - {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} превышена'
        else:
            return f'Скорость {self.name} допустимая'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость SportCar {self.name} - {self.speed}')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость work car {self.name} - {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} превышена'
        else:
            return f'Скорость {self.name} допустимая'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        print(f'Текущая скорость police {self.name} - {self.speed}')


Volkswagen = TownCar(80, 'синяя', 'Volkswagen', False)
Ford = SportCar(130, 'красная', 'Ford Mustang', False)
WAZ = WorkCar(50, 'зелёная', 'УАЗ 2206', False)
BMW = PoliceCar(120, 'белая', 'BMW E65', True)
print(Volkswagen.turn_left())
print(f'Когда {BMW.turn_right()}, то {Ford.stop()}')
print(WAZ.show_speed())
print(BMW.show_speed())
print(Volkswagen.show_speed())