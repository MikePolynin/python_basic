def make_zip(a, b, index=0, result=None):
    if result is None:
        result = list()

    if index == min(len(a), len(b)):
        return result

    pair = (a[index], b[index])
    result.append(pair)
    print(pair)
    make_zip(a, b, index + 1, result)


def my_zip_2():
    input_string = input('Первый набор символов через запятую с пробелом: ').split(', ')
    input_tuple = input('Второй набор символов через запятую с пробелом: ').split(', ')

    print('\nРезультат:')
    make_zip(input_string, input_tuple)


my_zip_2()
