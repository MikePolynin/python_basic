from math import pi


class MyMath:
    @classmethod
    def circle_len(cls, radius: float):
        return round(pi * 2 * radius, 3)

    @classmethod
    def circle_sq(cls, radius: float):
        return round(pi * radius ** 2, 3)

    @classmethod
    def square_volume(cls, side: float) -> float:
        return round(side ** 3, 3)

    @classmethod
    def sphere_surface_sq(cls, radius: float):
        return round(pi * (2 * radius) ** 2, 3)
