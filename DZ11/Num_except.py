class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


list_of_nums = []
input_elem = str()
# запускаем цикл для заполнения списка, пока пользователь не введет stop
while not (input_elem == 'stop' or input_elem == 'Stop'):
    try:
        input_elem = input('Введите число: ')
        # если значение число вводим его в список
        if input_elem.isdigit():
            num_for_list = int(input_elem)
            list_of_nums.append(num_for_list)
        # если нет выводим ошибку и продолжаем ввод
        else:
            raise OwnError('Введено не число')
    except OwnError as e:
        print(e)
        continue
print(list_of_nums)
