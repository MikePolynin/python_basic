def competition_protocol():
    result_dict = dict()

    quantity = int(input('Сколько записей вносится в протокол? '))

    print('Записи (результат и имя): ')
    for i in range(quantity):
        result = input('{0} запись: '.format(i + 1))

        result_list = result.split(' ')

        if result_list[1] not in result_dict:
            result_dict[result_list[1]] = int(result_list[0])
        elif int(result_list[0]) > result_dict[result_list[1]]:
            result_dict[result_list[1]] = int(result_list[0])

    print('\nИтоги соревнований: ')
    for i in range(3):
        result = max(result_dict.values())

        for player in result_dict:
            if result_dict[player] == result:
                print('{0} место: {1} ({2})'.format(
                    i + 1,
                    player,
                    result_dict[player]
                ))
                result_dict[player] = 0


competition_protocol()
