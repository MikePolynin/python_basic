def contact_3():
    phone_book = {
        'Иванов': [['Павел', 12355555], ['Иван', 45688888]]
    }

    while True:
        choice = int(input('\nЧто делаем? 1 - добавить контакт, 2 - найти по фамилии: '))

        if choice == 1:
            name = input('Введите имя нового контакта: ')
            surname = input('Введите фамилию нового контакта: ')
            phone_number = input('Введите номер телефона нового контакта: ')

            if surname.title() in phone_book:
                exist = False
                for contact in phone_book[surname.title()]:
                    if contact[0] == name.title():
                        print('Такой контакт уже есть')
                        exist = True
                        break
                if not exist:
                    phone_book[surname.title()].append([name.title(), int(phone_number)])
            else:
                phone_book[surname.title()] = [[name.title(), int(phone_number)]]

            print('Контакты:')
            for surname, data in phone_book.items():
                for contact in data:
                    print(surname, contact[0], contact[1])

        elif choice == 2:
            surname = input('Введите фамилию для поиска контакта: ')

            if surname.title() in phone_book:
                print('Результат поиска:')
                for contact in phone_book[surname.title()]:
                    print(surname.title(), contact[0], contact[1])
            else:
                print('Такой фамилии нет в контактах')


contact_3()
