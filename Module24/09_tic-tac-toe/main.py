def print_field(elems):
    print()
    count = 0
    for line in range(3):
        for elem in range(3):
            print('{:^4}'.format(elems[count]), end='')
            count += 1
        print()


def move(elems, x_o):
    while True:
        cell = input('\nКуда поставить {}? '.format(x_o))
        if not cell.isdigit():
            print('Некорректный ввод')
        elif 0 >= int(cell) or int(cell) > 9:
            print('Некорректный ввод')
        elif isinstance(elems[int(cell) - 1], str):
            print('Некорректный ввод')
        else:
            elems[int(cell) - 1] = x_o
            print_field(elems)
            return int(cell)


def check_end(candidate, x, o):
    winner_set = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
    for win_set in winner_set:
        if win_set <= candidate[1]:
            print('\nПобеда {}'.format(candidate[0]))
            return True
    if len(x) + len(o) == 9:
        print('\nХодов больше нет')
        return True
    return False


def tic_tac_toe():
    elems = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = set()
    o = set()
    print_field(elems)

    while True:
        x.add(move(elems, 'X'))
        if check_end(['X', x], x, o):
            break
        o.add(move(elems, 'O'))
        if check_end(['O', o], x, o):
            break


tic_tac_toe()
