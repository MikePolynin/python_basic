import random


def entertainment():
    sticks_qty = int(input('Кол-во палок: '))
    threw_qty = int(input('Кол-во бросков: '))

    result = ['I' for _ in range(sticks_qty)]

    for i in range(threw_qty):
        r_i = random.randint(1, sticks_qty + 1)
        l_i = random.randint(1, r_i)

        result = ['.' if l_i <= i + 1 <= r_i else result[i] for i in range(sticks_qty)]

        print('Бросок', i + 1, '. Сбиты палки с номера', l_i, 'по номер', r_i)

    print('\nРезультат: ' + str.join('', result))


entertainment()
