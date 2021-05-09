list_of_prices = (input('Введите цены на товар в формате 57.8, 46.51, 97...: ')).split(', ')
price_in_string = 'Цены: '

for elem_of_list in list_of_prices:
    elem_of_list = elem_of_list.split('.')
    if len(elem_of_list) > 1 and len(elem_of_list[1]) < 2:
        rub, kop = elem_of_list[0], int(elem_of_list[1])
        price = f'{rub} руб {kop:<02d} коп'
        price_in_string += price
        price_in_string += ', '
    elif len(elem_of_list) > 1 and len(elem_of_list[1]) == 2:
        rub, kop = elem_of_list[0], elem_of_list[1]
        price = f'{rub} руб {kop} коп'
        price_in_string += price
        price_in_string += ', '
    else:
        rub = elem_of_list[0]
        price = f'{rub} руб 00 коп'
        price_in_string += price
        price_in_string += ', '   # думал избавиться от конкатенации с помощью join, но не вышло
print(price_in_string)
# Смотрим id списка
print(id(list_of_prices))
# Сортируем по возрастанию
list_of_prices.sort()
# Вывод по возрастанию и сверяем id
print(list_of_prices, id(list_of_prices))
# Тут же сделаем срез для пяти товаров если список идет на возрастание
if len(list_of_prices) >= 5:
    print("Пять самых дорогих товаров по возрастанию: ", list_of_prices[-5:])
else:
    print("Самые дорогие товары по возрастанию: ", list_of_prices)  # на случай если список небольшой
# Делаем reverse для сортировки по убыванию
list_of_prices.reverse()
print(list_of_prices)
# Делаем срез для пяти самых дорогих товаров, если список идет на убывание
if len(list_of_prices) >= 5:
    print("Пять самых дорогих товаров по убыванию: ", list_of_prices[:5])
else:
    print("Самые дорогие товары по убыванию: ", list_of_prices)


