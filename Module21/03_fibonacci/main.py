def get_fib_number(num_pos, prev_number=1, number=1, number_index=0):
    if number_index == int(num_pos):
        print('\nЧисло:', number)
        return number
    get_fib_number(num_pos=num_pos, prev_number=number, number=prev_number + number, number_index=number_index + 1)


def fibonacci():
    num_pos = input('Введите позицию числа в ряде Фибоначчи: ')

    get_fib_number(num_pos)


fibonacci()
