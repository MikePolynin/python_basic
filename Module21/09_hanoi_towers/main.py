def move(quantity, from_where, where):
    middle = 6 - from_where - where

    if quantity >= 1:
        move(quantity - 1, from_where, middle)

        print('Переложить диск {0} со стержня номер {1} на стержень номер {2}'.format(
            quantity,
            from_where,
            where))

        move(quantity - 1, middle, where)


def hanoi_towers():
    quantity = int(input('Введите количество дисков: '))

    move(quantity, 1, 2)


hanoi_towers()
