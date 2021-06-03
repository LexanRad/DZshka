# создаем класс дорога
class Road:
    # даем атрибуты длина и ширина
    _length = 0
    _width = 0

    # создаем метод для записи атрибутов для экземпляра
    def __init__(self, length, width):
        self._length = length
        self._width = width

    # создаем метод расчета
    def mass_of_asphalt(self):
        # задаем массу асфальта на квадратный метр и толщину/глубину
        mass_for_cube = 25
        depth_of_asphalt = 5
        # высчитываем и возвращаем массу
        mass = (self._length * self._width * mass_for_cube * depth_of_asphalt) // 1000
        return mass


asphalt = Road(20, 5000)
print(asphalt.mass_of_asphalt(), 'т')
