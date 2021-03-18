def get_fib_number(num_pos, prev_number=1, number=1, number_index=2):
    if int(num_pos) == 0 or int(num_pos) == 1:
        return 1
    elif number_index == int(num_pos):
        return number
    else:
        return get_fib_number(num_pos=num_pos,
                              prev_number=number,
                              number=prev_number + number,
                              number_index=number_index + 1)


def fibonacci():
    num_pos = input('Введите позицию числа в ряде Фибоначчи: ')

    return get_fib_number(num_pos)


print('\nЧисло:', fibonacci())
