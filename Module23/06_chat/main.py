def chat():
    name = input('Введите имя пользователя: ')
    print()

    while True:
        print('Выберите действие 1 или 2:\n'
              '1 - Посмотреть текущий текст чата\n'
              '2 - Отправить сообщение')
        choice = int(input('Ваш выбор: '))
        try:
            if choice == 1:
                with open('chat.txt', 'r', encoding='utf-8') as chat_list:
                    print('\nТекст чата:')
                    print(chat_list.read())
            elif choice == 2:
                with open('chat.txt', 'a', encoding='utf-8') as chat_list:
                    message = input('\nВведите сообщение:\n')
                    chat_list.write(name + ': ' + message + '\n')
                    print()
            else:
                raise ValueError
        except ValueError:
            print('Некорректный ввод')


chat()
