weather_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

weather_string = " ".join(weather_list)
# Форматируем строку с помощью replace. Т.к. 5 везде заменяется на 05 - с градусами поступаем так ('+"05"', '"+05"')
for elem in (('5', '"05"'), ('17', '"17"'), ('+"05"', '"+05"')):
    weather_string = weather_string.replace(*elem)

print(weather_string)
# pull
