def frequency_hist_2():
    input_string = input('Введите текст: ')

    letter_dict = dict()
    unique_letters = []
    letter_list = []

    for symbol in input_string:
        if symbol in letter_dict:
            letter_dict[symbol] = letter_dict.pop(symbol) + 1
        else:
            letter_dict[symbol] = 1

    print('Оригинальный словарь частот:')

    for key in letter_dict:
        print(key, ':', letter_dict[key])

    for value in letter_dict.values():
        if value not in unique_letters:
            unique_letters.append(value)

    print('\nИнвертированный словарь частот:')

    for value in unique_letters:
        letter_list.clear()
        for key in letter_dict.keys():
            if letter_dict[key] == value:
                letter_list.append(key)
        print(value, ':', letter_list)


frequency_hist_2()
