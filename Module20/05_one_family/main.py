def one_family():
    families = {'Сидоров Никита': 35, 'Сидорова Алина': 34, 'Сидоров Павел': 10,
                'Иванов Павел': 18, 'Иванова Надежда': 19, 'Иванов Андрей': 20,
                'Петров Иван': 30, 'Петрова Светлана': 31, 'Петров Сергей': 32}

    surname = input('Введите фамилию: ')
    print()

    for family in families:
        if surname.title() in family:
            print(family)


one_family()
