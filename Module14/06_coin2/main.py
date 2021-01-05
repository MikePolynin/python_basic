def coin_search():
    print('Введите координаты монетки:')
    x = float(input('X: '))
    y = float(input('Y: '))
    radius = int(input('Введите радиус: '))

    circle = (x ** 2 + y ** 2) ** 0.5

    if circle <= radius:
        print('\nМонетка где-то рядом')
    else:
        print('\nМонетки в области нет')


coin_search()
