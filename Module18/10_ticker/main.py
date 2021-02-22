def ticker():
    first_string = input('Первая строка: ')
    second_string = input('Вторая строка: ')

    the_same = False
    step = 0

    if len(first_string) != len(second_string):
        print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')
    else:
        for i in range(len(second_string)):
            check_string = second_string[i:] + second_string[0:i]
            if first_string == check_string:
                the_same = True
                step = i
                break

    if not the_same:
        print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')
    else:
        print('\nПервая строка получается из второй со сдвигом {}.'.format(
            step
        ))


ticker()
