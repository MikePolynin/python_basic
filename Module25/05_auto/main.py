from bus import Bus


def auto():
    my_bus = Bus([2, 5], 30)

    print('Изначально')
    print(my_bus.coordinates)
    print(my_bus.corner)
    print(my_bus.passengers)
    print(my_bus.money)

    my_bus.move(20)

    print('После движения пустым')
    print(my_bus.coordinates)
    print(my_bus.corner)
    print(my_bus.passengers)
    print(my_bus.money)

    my_bus.turn(15)

    print('После поворота')
    print(my_bus.coordinates)
    print(my_bus.corner)
    print(my_bus.passengers)
    print(my_bus.money)

    my_bus.get_in(10)

    print('После посадки')
    print(my_bus.coordinates)
    print(my_bus.corner)
    print(my_bus.passengers)
    print(my_bus.money)

    my_bus.get_out(5)

    print('После высадки')
    print(my_bus.coordinates)
    print(my_bus.corner)
    print(my_bus.passengers)
    print(my_bus.money)

    my_bus.move(20)

    print('После движения с пассажирами')
    print(my_bus.coordinates)
    print(my_bus.corner)
    print(my_bus.passengers)
    print(my_bus.money)


auto()
