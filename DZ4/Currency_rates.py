from requests import api


def currency_rates(name_currency):
    """
    Function that uses module 'requests' for get currency rate from http://www.cbr.ru/scripts/XML_daily.asp
    :param name_currency: abbreviation of name of currency (USD, GBP, etc.)
    :return: rate of needed currency, OR 'None', if currency not exist/incorrect name
    """
    # приводим валюту к верхнему регистру
    name_currency = name_currency.upper()
    # получаем контент с сайта, приводим сначала к строке, а потом к списку (в качестве разделителя послужат ><)
    content_currency = api.get('http://www.cbr.ru/scripts/XML_daily.asp').text.split('><')
    # получаем из списка дату. Не знаю как правильно ее привести к объекту date
    date = content_currency[1].split('"')[1]
    # выставим курс по умолчанию на none
    value_of_currency = None
    # перебираем список в поиске искомой валюты
    for elem_of_content in content_currency:
        if elem_of_content == f'CharCode>{name_currency}</CharCode':
            # выдергиваем индекс элемента с названием валюты
            index_of_elem = content_currency.index(elem_of_content)
            # используем его, чтобы найти сам курс (курс находится через три элемента списка), делаем срез лишнего
            value_of_currency = content_currency[index_of_elem + 3][6:-7]
    # если валюта нашлась, то печатаем ее и дату
    if value_of_currency is not None:
        print(value_of_currency, ' рублей на момент: ', date)
    # если нет выводим none
    else:
        print('None')


currency_rates('usd')
currency_rates('eur')
