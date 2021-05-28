import os


def dict_write_size_files(min_size_threshold, max_size_threshold):
    """
    Function for write pairs key:value in dict
    :param min_size_threshold: min size of file
    :param max_size_threshold: max size of file
    :return:
    """
    key = max_size_threshold
    values = 0
    for file in os.scandir(folder):
        if min_size_threshold <= file.stat().st_size < max_size_threshold:
            values += 1
    dict_of_files[key] = values


# Пилим пустой словарь
dict_of_files = {}
# пытаемся запилить пары ключ:значение в него. Try для пробы
try:
    # взял some_data из материалов урока
    folder = 'some_data'
    # вызываем функцию, давая ей значения минимума и максимума размера
    dict_write_size_files(0, 100)
    dict_write_size_files(100, 1000)
    dict_write_size_files(1000, 10000)
    dict_write_size_files(10000, 100000)
    print(dict_of_files)
except FileNotFoundError as e:
    print(f'concrete error: {e}')
except Exception as e:
    print(f'global error: {e}')
