def get_jokes(num_of_jokes):
    """
    Фунция, выдающая шутеечки на выходе
    :param num_of_jokes: кол-во шутеечек
    :return:
    """
    from random import choice
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for joke in range(0, num_of_jokes):
        print(choice(nouns), choice(adverbs), choice(adjectives))


n = int(input('Сколько шуток хотите? '))
get_jokes(n)
