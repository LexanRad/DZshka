duration = int(input('Введите duration: '))

if duration >= 0:
    days = duration // 86400
    hours = (duration % 86400) // 3600
    minutes = ((duration % 86400) % 3600) // 60
    seconds = ((duration % 86400) % 3600) % 60
    print(days, "дн", hours, "ч", minutes, "мин", seconds, "сек")
else:
    print("Неккоректный duration")

# Изначально был длинный код, который выводил print без дней, часов, и минут (если duration был не такой большой),
# но поняв, что в каждом elif убирается лишь пара строк, и вспомнив Дзен Питона, решил убрать. Догадываюсь, что можно
# было и короче, с удовольствием узнаю как
