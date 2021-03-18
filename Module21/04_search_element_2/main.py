def searching(user_key, this_dict, user_depth, depth=1):
    if user_key in this_dict.keys():
        print('\nРезультат поиска:', this_dict[user_key])
    elif user_depth < depth and user_depth != 0:
        print('\nКлюча {0} не найдено'.format(user_key))
    else:
        for value in this_dict.values():
            if isinstance(value, dict):
                searching(user_key, value, user_depth, depth + 1)
                break
            print('\nКлюча {0} не найдено'.format(user_key))


def search_element_2():
    user_key = input('Введите ключ для поиска: ')

    depth = int(input('Хотите ввести глубину поиска? 1 - да, 0 - нет: '))
    if depth == 1:
        user_depth = int(input('Введите глубину поиска. 0 - бесконечность: '))
    else:
        user_depth = 0

    site = {
        'html': {
            'head': {
                'title': 'Мой сайт'
            },
            'body': {
                'h2': 'Здесь будет мой заголовок',
                'div': 'Тут, наверное, какой-то блок',
                'p': 'А вот здесь новый абзац'
            }
        }
    }

    searching(user_key, site, user_depth)


search_element_2()
