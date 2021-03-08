def make_zip(a, b):
    return [(a[i], b[i]) for i in range(min(len(a), len(b)))]


def my_zip():
    input_string = input('Строка: ')
    input_tuple = tuple(input('Кортеж чисел: ').split(', '))

    print(input_tuple)
    print(input_tuple[0])

    # pairs = zip(input_string, input_tuple)
    pairs = make_zip(input_string, input_tuple)

    print('\nРезультат:')
    for pair in pairs:
        print(pair)


my_zip()
