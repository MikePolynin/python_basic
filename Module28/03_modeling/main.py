from figures import Cube, Pyramid


def modeling():
    my_cube = Cube(5)
    print(my_cube.area_3d())

    my_pyramid = Pyramid(6, 4)
    print(my_pyramid.area_3d())


modeling()
