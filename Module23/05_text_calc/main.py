def calc():
    total_sum = 0
    try:
        with open('calc.txt', 'r') as data:
            for index, func in enumerate(data):
                try:
                    func_list = str(func).split(' ')
                    if func_list[1] == '+':
                        total_sum += int(func_list[0]) + int(func_list[2])
                    elif func_list[1] == '-':
                        total_sum += int(func_list[0]) - int(func_list[2])
                    elif func_list[1] == '*':
                        total_sum += int(func_list[0]) * int(func_list[2])
                    elif func_list[1] == '/':
                        total_sum += int(func_list[0]) / int(func_list[2])
                    elif func_list[1] == '//':
                        total_sum += int(func_list[0]) // int(func_list[2])
                    elif func_list[1] == '%':
                        total_sum += int(func_list[0]) % int(func_list[2])
                    else:
                        raise ValueError
                except ZeroDivisionError:
                    print('В строке {} деление на ноль'.format(index + 1))
                except IndexError:
                    print('В строке {} не хватает данных'.format(index + 1))
                except ValueError:
                    print('В строке {} некорректные данные'.format(index + 1))
        print('\nСумма результатов корректных выражений:', total_sum)
    except FileNotFoundError:
        print('Файл с выражениями не найден')


calc()
