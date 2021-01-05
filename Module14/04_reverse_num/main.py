def reverse():
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')

    dec = a.index('.')
    n_1 = a[dec - 1:: -1]
    n_2 = a[:dec: -1]
    reverse_a = n_1 + '.' + n_2

    dec = b.index('.')
    n_1 = b[dec - 1:: -1]
    n_2 = b[:dec: -1]
    reverse_b = n_1 + '.' + n_2

    summ = float(reverse_a) + float(reverse_b)

    print('\nПервое число наоборот:', reverse_a)
    print('Второе число наоборот:', reverse_b)
    print('Сумма:', summ)


reverse()
