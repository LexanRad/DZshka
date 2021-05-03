numbers = range(1, 1000)
list_of_cubs = []

for number in numbers:
    # Берем нечетные числа
    if number % 2 != 0:
        # Возводим в куб, прибавляем 17 (пункт b).
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
# Вычисляем сумму (задание a). Есть новая переменная, но не список (задание c)
amount_of_cubs = 0

for count in list_of_cubs:
    amount_of_cubs += count

print(amount_of_cubs)
