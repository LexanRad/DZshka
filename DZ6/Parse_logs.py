from requests import api

logs = api.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text
# здесь создал файл логов из ссылки. В принципе api нужен был только для этого
# with open('Logs.txt', 'w', encoding='utf-8') as f:
#     f.writelines(logs)
list_of_tuples = []
with open('logs.txt', 'r', encoding='utf-8') as f:
    # Формируем списки из строк
    for line in f:
        list_of_line = f.readline().split(' ', maxsplit=7)
        # Удаляем лишнее
        del list_of_line[1:5]
        del list_of_line[-1]
        # обращаем списки в кортежи и передаем в основной список
        list_of_tuples.append(tuple(list_of_line))
print(*list_of_tuples, sep=',\n')
