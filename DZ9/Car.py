# как и в предыдущих заданиях создаем класс и инит
class Car:
    speed = 0
    # добавил значение ограничения скорости для show_speed
    speed_limit = None
    color = 'some_color'
    name = 'some_name'
    is_police = False

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

    # пилим методы
    def go(self):
        print(self.name, 'поехала')

    def stop(self):
        print(self.name, 'остановилась')

    def turn(self, direction):
        print(self.name, 'повернула', direction)

    def show_speed(self):
        print(self.speed, 'км/ч')
        if self.speed_limit < self.speed:
            print('Скорость превышена')


# создаем дочерние классы
class TownCar(Car):
    speed_limit = 60


class SportCar(Car):
    speed_limit = 80


class WorkCar(Car):
    speed_limit = 40


class PoliceCar(Car):
    is_police = True
    speed_limit = 80


# проверяем
a = TownCar('Audi', 'red', 70)
a.go()
a.turn('налево')
a.show_speed()
a.stop()
b = WorkCar('Mercedes', 'grey', 40)
b.go()
b.turn('направо')
b.show_speed()
b.stop()
