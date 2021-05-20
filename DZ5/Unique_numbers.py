from collections import Counter


def list_unique(list_of_numbers):
    """
    Function that remove all duplicate numbers
    :param list_of_numbers: original list
    :return: list of unique numbers
    """
    # для решения взял Counter из модуля collections, который позволяет высчитывать уникальные элементы
    numbers = Counter(list_of_numbers)
    unique_numbers = [num_index for num_index in list_of_numbers if numbers[num_index] == 1]
    return unique_numbers


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(list_unique(src))
