# Создаем пустой словарь, в который и будем писать ключ: значение из файлов names и hobby's
dict_of_hobby = {}
# открываем оба файла
with open('Names.txt', 'r', encoding='utf-8') as f1:
    with open("Hobby's.txt", 'r', encoding='utf-8') as f2:
        # Создаем листы имен и хобби
        list_of_names = f1.readlines()
        list_of_hobby = f2.readlines()
        # Сравниваем длинну этих листов.
        if len(list_of_names) >= len(list_of_hobby):
            # если длина имен больше или равна длине хобби, то добавляем пару ключ: значение, не забывая убрать лишнее
            # в строке (перенос \n)
            for index in range(len(list_of_names)):
                if index < len(list_of_hobby):
                    dict_of_hobby.setdefault(
                        list_of_names[index].replace('\n', ''), [list_of_hobby[index].replace('\n', '')]
                    )
                else:
                    # по условию если имен больше чем хобби - делаем значение None
                    dict_of_hobby.setdefault(list_of_names[index].replace('\n', ''), [None])
        else:
            # В случае если хобби больше чем имен, выходим в exit code 1
            print("Oopsie, there is so much hobby's")
            quit(1)
# записываем каждую пару ключ: значение в файл. Не смог разобраться как сохранить сам словарь.
# если сохранять именно словарь - пропадают значения, через модуль пикл - получается полу-эльфийский
with open('Dict_of_hobby.txt', 'w', encoding='utf-8') as f:
    for key, value in dict_of_hobby.items():
        f.write(f'{key} - {value}\n')
