# все по аналогии с предыдущими заданиями
class Worker:
    name = 'some_name'
    surname = 'some_surname'
    position = 'some_position'
    _income = {"wage": 'wage', "bonus": 'bonus'}

    def __init__(self, name, surname, position, income):
        try:
            self.name = name
            self.surname = surname
            self.position = position
            self._income = {"wage": income[0], "bonus": income[1]}
        # добавим исключение если income не список
        except TypeError as e:
            print('income must be a list: ', e)


# создаем класс позиция, передаем наследство от воркера
class Position(Worker):
    # пилим метод на полное имя
    def get_full_name(self):
        print(self.name, self.surname)

    # пилим метод на прибыль
    def get_total_income(self):
        total = self._income["wage"] + self._income["bonus"]
        print(total, 'руб')


# видим в выводе что все окэ, position унаследовала от  worker'а аттрибуты и init
a = Position('Lexan', 'Rad', 'programmer', [40000, 15000])
a.get_full_name()
a.get_total_income()
