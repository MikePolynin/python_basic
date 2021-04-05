def counting(func):
    func_list = str(func).split(' ')
    if func_list[1] == '+':
        return int(func_list[0]) + int(func_list[2])
    elif func_list[1] == '-':
        return int(func_list[0]) - int(func_list[2])
    elif func_list[1] == '*':
        return int(func_list[0]) * int(func_list[2])
    elif func_list[1] == '/':
        return int(func_list[0]) / int(func_list[2])
    elif func_list[1] == '//':
        return int(func_list[0]) // int(func_list[2])
    elif func_list[1] == '%':
        return int(func_list[0]) % int(func_list[2])
    else:
        raise ValueError


def text_calc_2():
    total_sum = 0
    try:
        with open('calc.txt', 'r') as data:
            for func in data:
                try:
                    total_sum += counting(func)
                except (ZeroDivisionError, IndexError, ValueError):
                    print('\nОбнаружена ошибка в строке: {}'.format(func.replace('\n', '')))
                    choice = input('Хотите исправить? да/ нет ')
                    if choice.lower() == 'да':
                        new_func = input('Введите исправленную строку: ')
                        total_sum += counting(new_func)
        print('\nСумма результатов корректных выражений:', total_sum)
    except FileNotFoundError:
        print('Файл с выражениями не найден')


text_calc_2()
