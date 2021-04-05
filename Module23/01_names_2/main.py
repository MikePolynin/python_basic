def names_2():
    open('errors.log', 'w').close()
    total_length = 0
    line_count = 0
    try:
        with open('people.txt', 'r', encoding='utf-8') as people:
            for line in people:
                line_count += 1
                length = len(line)
                if line.endswith('\n'):
                    length -= 1
                if length < 3:
                    error = 'Строка {} слишком коротка'.format(line_count)
                    print(error)
                    with open('errors.log', 'a', encoding='utf-8') as error_log:
                        error_log.write(error + '\n')
                else:
                    total_length += length
    except FileNotFoundError:
        print('Файл с именами не найден')
    finally:
        print('Сумма символов в строках с длиной больше 3: {0}'.format(total_length))


names_2()
