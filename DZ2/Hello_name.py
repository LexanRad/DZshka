names_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
              'директор аэлита']

for elem_of_list in names_list:
    # Приводим элемент к заглавным буквам, разделяем строку на список, вытаскиваем последний элемент - Имя
    name_in_str = elem_of_list.title().split().pop()
    print('Привет,', name_in_str, '!')

#Для pulla
