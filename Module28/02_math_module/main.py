from my_math import MyMath


def math_module():
    res_1 = MyMath.circle_len(radius=5)
    res_2 = MyMath.circle_sq(radius=6)
    print(res_1)
    print(res_2)

    res_3 = MyMath.square_volume(side=8)
    res_4 = MyMath.sphere_surface_sq(radius=7)
    print(res_3)
    print(res_4)


math_module()