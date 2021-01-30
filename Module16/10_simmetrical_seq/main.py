def symmetrical_seq():
    seq = []
    seq_check = []
    seq_check_2 = []
    add = []

    quantity = int(input('Кол-во чисел: '))

    for i in range(quantity):
        digit = input('Число: ')
        seq.append(digit)

    for i in range(len(seq)):
        for j in range(i, len(seq)):
            seq_check.append(seq[j])

        for k in range(len(seq_check) - 1, -1, -1):
            seq_check_2.append(seq_check[k])

        if seq_check == seq_check_2:
            for m in range(i - 1, -1, -1):
                add.append(seq[m])
            break

        seq_check.clear()
        seq_check_2.clear()

    seq_str = ' '.join(seq)
    add_str = ' '.join(add)

    print('\nПоследовательность: ' + seq_str)
    print('Нужно приписать чисел:', len(add))
    if len(add) != 0:
        print('Сами числа: ' + add_str)


symmetrical_seq()
