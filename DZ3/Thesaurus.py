def thesaurus_adv(input_names):
    """
    Функция, забирающая из списка имена по букве
    :param input_names: строка с именами
    :return:
    """
    # разобьем строку в список, добавим пустой словарь для заполнения и список ключей к нему
    list_of_names = input_names.split(', ')
    dict_of_names = {}
    key_letters = []
    # Перебираем имена
    for name in list_of_names:
        # Т.к в строке первой идет кавычка, ключом будет буква по индексу [1]
        letter = name[1]
        # Проверяем начинается ли строка с этой буквы и есть ли буква в ключах.
        if name.startswith(letter, 1) and letter in key_letters:
            # если есть - добавляем в значение
            dict_of_names[letter].append(name)
        else:
            # если нет - записываем букву в ключи, создаем пару "ключ: значение" для словаря
            key_letters.append(letter)
            dict_of_names.setdefault(letter, [name])

    print(dict_of_names)


string_of_names = input('Введите имена в кавычках, через запятую ("Иван", "Зинаида", "Василий", и т.д.) : ')

thesaurus_adv(string_of_names)
