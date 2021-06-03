# импортируем из time метод sleep для задержки по времени между изменением цвета
from time import sleep


# создаем класс светофор
class TrafficLight:
    # даем атрибут цвет
    color = 'some_color'

    # создаем метод запуска
    def running(self):
        # делаем цикл
        while True:
            self.color = 'red'
            print(self.color)
            sleep(7)
            self.color = 'yellow'
            print(self.color)
            sleep(2)
            self.color = 'green'
            print(self.color)
            sleep(10)


# создаем сфетофор "а" и запускаем
a = TrafficLight()
a.running()
