def sort_function(input_tuple):
    input_list = list(input_tuple)
    result_list = []
    not_int = False

    for number in input_list:
        if not isinstance(number, int):
            not_int = True
            break

    if not_int:
        print('В кортеже {0} есть не целые числа'.format(input_tuple))
    else:
        while len(input_list) > 0:
            digit = min(input_list)
            result_list.append(digit)
            input_list.remove(digit)

        result_tuple = tuple(result_list)
        print('Отсортированный кортеж:', result_tuple)


sort_function((4, 3, 2, 6, 5))
