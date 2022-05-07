from time import sleep

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']
    def running(self):
        i = 0
        while True:
            if i == 0:
                print('Красный')
                sleep(7)
            elif i == 1:
                print('Желтый')
                sleep(2)
            elif i == 2:
                print('Зеленый')
                sleep(5)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()
