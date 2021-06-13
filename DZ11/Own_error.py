class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':
    try:
        num_1 = int(input('Введите первое число: '))
        num_2 = int(input('Введите второе число: '))
        if num_2 == 0:
            raise OwnError('Делить на ноль нельзя!')
        result = num_1 / num_2
        print(result)
    except ValueError:
        print('Введено не число')
    except OwnError as e:
        print(e)
