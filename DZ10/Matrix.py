import numpy as np  # модуль для данного случая. Почему бы не воспользоваться? Тем более что тз не говорит "нельзя")


class Matrix:
    matr = 'some_matrix'

    # используем numpy для создания матрицы
    def __init__(self, matrix_list):
        self.matr = np.matrix(matrix_list)

    # для вывода
    def __str__(self):
        return f'Матрица:\n {self.matr}'

    # для суммирования
    def __add__(self, other):
        amount_matr = self.matr + other.matr
        return f'Сумма матриц:\n {amount_matr}'


if __name__ == '__main__':
    a = Matrix([[1, 5, 6], [5, 6, 7]])
    b = Matrix([[10, 15, 9], [23, 65, 4]])
    print(a)
    print(b)
    print(a + b)
