from squares import Iterator, generator

max_int = int(input('Введите число: '))


def num_squares() -> None:
    print('\nIterator')

    my_iterator = Iterator(max_int)

    for number in my_iterator:
        print(number)

    print('\nGenerator')

    for number in generator(max_int):
        print(number)

    print('\nGenerator expression')

    squares = (number ** 2 for number in range(1, max_int + 1))
    for square in squares:
        print(square)


num_squares()
