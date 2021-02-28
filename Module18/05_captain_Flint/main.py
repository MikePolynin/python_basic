def capitan_Flint():
    x = 0
    y = 0

    oy = input('По оси OY: ')
    ox = input('По оси OX: ')

    coordinate_y = oy.split()
    coordinate_x = ox.split()

    if coordinate_y[0] == 'North':
        y += int(coordinate_y[1])
    elif coordinate_y[0] == 'South':
        y -= int(coordinate_y[1])
    else:
        print('Неверные координаты')

    if coordinate_x[0] == 'East':
        x += int(coordinate_x[1])
    elif coordinate_x[0] == 'West':
        x -= int(coordinate_x[1])
    else:
        print('Неверные координаты')

    print('\nКоординаты:', x, y)


capitan_Flint()
