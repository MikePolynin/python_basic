from circle import Circle


def circle():
    circle_1 = Circle(5, 4, 10)
    circle_2 = Circle(8, 6, 5)
    circle_3 = Circle()

    print(circle_1.find_perimeter())
    print(circle_2.find_square())
    print(circle_2.crossing(circle_3))
    print(circle_3.grow(15))
    print(circle_3.grow(1.1))
    print(circle_3.grow('a'))
    print(circle_2.crossing(circle_3))


circle()
