def friends():
    n = int(input('Кол-во друзей: '))
    k = int(input('Долговых расписок: '))

    count = 0
    result = [0] * n

    while count < k:
        print()
        print(count + 1, 'расписка')
        money_to = int(input('Кому: '))
        money_from = int(input('От кого: '))
        money_sum = int(input('Сколько: '))
        result[money_to - 1] -= money_sum
        result[money_from - 1] += money_sum
        count += 1

    print('\nБаланс друзей:')
    for i in range(n):
        print(i + 1, ':', result[i])


friends()
