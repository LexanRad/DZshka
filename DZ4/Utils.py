from requests import api


def currency_rates(input_name):
    """
    Function that uses module 'requests' for get currency rate from http://www.cbr.ru/scripts/XML_daily.asp
    :param name_currency: abbreviation of name of currency (USD, GBP, etc.)
    :return: rate of needed currency, OR 'None', if currency not exist/incorrect name
    """
    name_currency = input_name[1].upper()
    print(name_currency)
    content_currency = api.get('http://www.cbr.ru/scripts/XML_daily.asp').text.split('><')
    date = content_currency[1].split('"')[1]
    value_of_currency = None
    for elem_of_content in content_currency:
        if elem_of_content == f'CharCode>{name_currency}</CharCode':
            index_of_elem = content_currency.index(elem_of_content)
            value_of_currency = content_currency[index_of_elem + 3][6:-7]
    if value_of_currency is not None:
        print(value_of_currency, ' рублей на момент: ', date)
    else:
        print('None')


if __name__ == '__main__':
    import sys

exit(currency_rates(sys.argv))
