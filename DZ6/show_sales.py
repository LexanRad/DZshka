import sys
# окрываем файл
file_1 = open('bakery.csv', 'r', encoding='utf-8')
# достаем список
list_of_sales = file_1.readlines()
# редактируем сырые строки (избавляемся от лишних \n)
for sale in list_of_sales:
    sale.replace('\n', '')
# проверяем хотел ли пользователь узнать продажи в конкретном диапазоне
if len(sys.argv) == 3:
    # принтуем этот диапазон
    print(*list_of_sales[int(sys.argv[1]):int(sys.argv[2])], sep='')
# нет - принтуем весь лист
else:
    print(*list_of_sales, sep='')
