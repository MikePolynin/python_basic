def make_zip(a, b):
    result_list = []

    if len(a) > len(b):
        result_len = len(b)
    else:
        result_len = len(a)

    for i in range(result_len):
        pair = (a[i], b[i])
        result_list.append(pair)

    return result_list


def my_zip():
    input_string = input('Строка: ')
    input_tuple = input('Кортеж чисел: ')

    # pairs = zip(input_string, input_tuple)
    pairs = make_zip(input_string, input_tuple)

    print('\nРезультат:')
    print(pairs)

    for pair in pairs:
        print(pair)


my_zip()
