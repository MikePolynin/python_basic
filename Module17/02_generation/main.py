def generation():
    length = int(input('Введите длину списка: '))

    result = [1 if i % 2 == 0 else i % 5 for i in range(length)]

    print('Результат:', result)


generation()
