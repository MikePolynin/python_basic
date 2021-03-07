def pairs():
    input_str = input('Введите список из 10 чисел через пробел:')
    input_list = input_str.split(' ')

    result_list = [(input_list[i * 2], input_list[i * 2 + 1]) for i in range(5)]

    print('Оригинальный список:', input_list)
    print('Новый список:', result_list)


pairs()
