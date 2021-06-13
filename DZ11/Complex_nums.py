# вот тут есть одна запара, с которой так и не справился. Чарм упорно твердит что other.b не заполнен. прошерстил
# гугОл и так ничего не нашел
class ComplexNumber:
    i = 1

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Комплексное число: ({self.a} + {self.b}*{self.i})'

    def __add__(self, other):
        return ComplexNumber((self.a + other.a) + (self.b + other.b)*self.i)

    def __mul__(self, other):
        return ComplexNumber((self.a * other.a - self.a * other.a) + (other.a * self.b + self.a * other.b) * self.i)


first_num = ComplexNumber(10, 5)
print(first_num)
second_num = ComplexNumber(11, 3)
print(second_num)
print(first_num + second_num)
print(first_num * second_num)
