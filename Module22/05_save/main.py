import os


def save():
    text = input('Введите строку: ')
    user_path = input('\nКуда хотите сохранить документ? Введите последовательность папок (через пробел):\n')
    file_name = input('\nВведите имя файла: ')

    result = os.path.join(*user_path.split(' '), file_name + '.txt')

    if os.path.exists(result):
        user_file = open(result, 'w')

        if os.path.getsize(result) == 0:
            user_file.write(text)
            print('Файл успешно сохранён!')

        else:
            rewrite = input('Вы действительно хотите перезаписать файл? ')
            if rewrite == 'да' or rewrite == 'Да':
                user_file.write(text)
                print('Файл успешно перезаписан!')

            else:
                print('Файл не перезаписан')

        user_file.close()

    else:
        print('Некорректный путь')


save()
