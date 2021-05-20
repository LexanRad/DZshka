def greater_number(list_of_numbers):
    """
    Function that return list of greater numbers from original list
    :param list_of_numbers: original list
    :return: list of greater numbers
    """

    # создаем новый список через comprehension (count - индекс в диапазоне длины оригинального списка, условие if
    # сравнивает элемент с предыдущим)
    great_numbers = [list_of_numbers[count] for count in range(1, len(list_of_numbers))
                     if list_of_numbers[count] > list_of_numbers[count - 1]]
    return great_numbers


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(greater_number(src))
