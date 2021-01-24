def unique_elements():
    list_1 = []
    list_2 = []

    print('Заполнение 1 списка:')
    for _ in range(3):
        digit = int(input('Введите число: '))
        list_1.append(digit)

    print('\nЗаполнение 2 списка:')
    for _ in range(7):
        digit = int(input('Введите число: '))
        list_2.append(digit)

    print('\nПервый список:', list_1)
    print('Второй список:', list_2)

    list_1.extend(list_2)
    list_1 = set(list_1)

    print('\nНовый первый список с уникальными элементами:', list_1)


unique_elements()
