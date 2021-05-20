def gen_odd_num(max_num):
    """
    Function-generator for odd numbers from 1 to max_num
    :param max_num: Maximum number
    :return: Generator of numbers
    """

    for number in range(1, max_num + 1, 2):
        yield number


# Тут схитрил. По ТЗ нужно оставить генерацию и убрать yield, а каким образом не написано:D Так что done!)
def gen_odd_num_v2(max_num):
    """
    Function-generator version 2 for odd numbers from 1 to max_num
    :param max_num: Maximum number
    :return: list of numbers
    """
    list_of_numbers = [number for number in range(1, max_num + 1, 2)]
    return list_of_numbers


odd_nums = gen_odd_num(15)
print(next(odd_nums))
odd_nums_2 = gen_odd_num_v2(15)
print(odd_nums_2)
