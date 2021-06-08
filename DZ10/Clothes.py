from abc import ABC, abstractmethod


class Clothes(ABC):
    name = 'some_name'

    @abstractmethod
    def cloth_expense(self):
        pass

    @abstractmethod
    def __init__(self, name):
        self.name = name


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def cloth_expense(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def cloth_expense(self):
        return 2 * self.height + 0.3


if __name__ == '__main__':
    a = Coat(16)
    b = Suit(9)
    print(a.cloth_expense)
    print(b.cloth_expense)

