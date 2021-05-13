def num_translate_adv(number, language):
    """
    Функция для перевода чисел от 0 до 10 на английский или русский
    :param number: само число в буквенном формате
    :param language: язык на который будет переведено. Может принять значение en(если на английский), ru(на русский)
    :return:
    """
    # Создаем словарь с переводом
    dict_for_translate = {
        'zero': 'ноль', 'Zero': 'Ноль', 'one': 'один', 'One': 'Один', 'two': 'два', 'Two': 'Два', 'three': 'три',
        'Three': 'Три', 'four': 'четыре', 'Four': 'Четыре', 'five': 'пять', 'Five': 'Пять', 'six': 'шесть',
        'Six': 'Шесть', 'seven': 'семь', 'Seven': 'Семь', 'eight': 'восемь', 'Eight': 'Восемь', 'nine': 'девять',
        'Nine': 'Девять', 'ten': 'десять', 'Ten': 'Десять'
    }
    # Вытаскиваем значение по ключу, не забывая на какой язык будем переводить
    if language == 'ru':
        print(dict_for_translate.get(number))
    elif language == 'en':
        # меняем местами в словаре ключи и значения
        dict_for_translate = dict(zip(dict_for_translate.values(), dict_for_translate.keys()))
        print(dict_for_translate.get(number))
    else:
        # на случай ошибки в воде языка
        print('неккоректный ввод языка перевода')


num = input("Введите буквенно число: ")
lang = input("На какой язык переводим? (en - английский, ru - русский)")
num_translate_adv(num, lang)