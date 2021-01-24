def party():
    guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

    while True:
        print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
        user_input = input('Гость пришел или ушел? ')

        if user_input == 'пришел' or user_input == 'Пришел':
            name = input('Имя гостя: ')
            if len(guests) < 6:
                print('Привет, ' + name)
                guests.append(name)
            else:
                print('Прости, ' + name + ', но мест нет.')

        elif user_input == 'ушел' or user_input == 'Ушел':
            name = input('Имя гостя: ')
            print('Пока, ' + name + '!')
            guests.remove(name)

        elif user_input == 'пора спать' or user_input == 'Пора спать':
            print('\nВечеринка закончилась, все легли спать.')
            break

        else:
            print('Некорректный ввод')


party()
