from itertools import zip_longest


def gen_tuples(first_list, second_list):
    """
    Function-generator of tuples from two lists
    :param first_list: list of first elements of tuples
    :param second_list: list of second elements of tuples
    :return: generator of tuples
    """

    # Хотел пихнуть if в сам генератор, но не получилось, к тому же, как по мне, страдает от этого читабельность из-за
    # нагромождения. Проверяем длинее ли первый список т.к. в нем содержатся имена
    if len(first_list) > len(second_list):
        # Если да, то берем функцию zip_longest из itertools и дополняем кортежи без элемента второго списка None-ом
        for tuple_tutor_class in zip_longest(first_list, second_list, fillvalue=None):
            yield tuple_tutor_class
    # В других случаях используем простой zip. Если второй лист больше первого - генератор не сгенирирует кортеж
    # без отсутствующего элемента
    else:
        for tuple_tutor_class in zip(first_list, second_list):
            yield tuple_tutor_class


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
tuples = gen_tuples(tutors, klasses)
print(type(tuples))  # доказательство, что это генератор
print(next(tuples))
print(next(tuples))
print(next(tuples))
print(next(tuples))
print(next(tuples))
print(next(tuples))
print(next(tuples))
print(next(tuples))
