class Stationery:
    title = 'some_title'

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск написания')


class Pencil(Stationery):
    def draw(self):
        print('Запуск черчения')


class Handle(Stationery):
    def draw(self):
        print('Запуск разметки')


a = Handle('маркер')
a.draw()
b = Pencil('карандаш')
b.draw()
c = Pen('ручка')
c.draw()
