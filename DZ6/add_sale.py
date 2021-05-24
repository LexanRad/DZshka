import sys
# тут все просто: открываем файл записываем в него выражение в конец (доступ 'а')
with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.writelines(f'{sys.argv[1]}\n')
    print('Done')
