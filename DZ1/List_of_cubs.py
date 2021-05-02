numbers = range(1, 1000)
list_of_cubs = []

for number in numbers:
    # Берем нечетные числа
    if number % 2 != 0:
        # Возводим в куб (пункт a задания), прибавляем 17 (пункт b). Новый список не создан (пункт c)
        number = number**3 + 17
        # складываем нехитрыми манипуляциями в цикле while, где num само число для цикла, amount - сумма элементов
        num = number
        amount = 0
        while num != 0:
            amount = amount + num % 10
            num = num // 10
        # проверяем делится ли на 7 без остатка, если делится заносим в список
        if amount % 7 == 0:
            list_of_cubs.append(number)
print(list_of_cubs)