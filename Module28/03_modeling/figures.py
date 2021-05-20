class Square:
    def __init__(self, side: float) -> None:
        self._side = side

    def perimeter(self) -> float:
        return self._side * 4

    def area_2d(self) -> float:
        return self._side ** 2

    @property
    def side(self) -> float:
        return self._side

    @side.setter
    def side(self, side: float) -> None:
        self._side = side


class Triangle:
    def __init__(self, base: float, height: float) -> None:
        self._base = base
        self._height = height

    @property
    def base(self) -> float:
        return self._base

    @base.setter
    def base(self, base: float) -> None:
        self._base = base

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, height: float) -> None:
        self._height = height

    def perimeter(self) -> float:
        return round(((self._base / 2) ** 2 + self._height ** 2) ** 0.5 ** 2 + self._base, 3)

    def area_2d(self) -> float:
        return round(self._base * self._height / 2, 3)


class Cube(Square):
    def __init__(self, side: float) -> None:
        for _ in range(6):
            super().__init__(side)

    def area_3d(self) -> float:
        return self.area_2d() * 6


class Pyramid(Triangle):
    def __init__(self, base: float, height: float) -> None:
        for _ in range(4):
            super().__init__(base, height)

    def area_3d(self) -> float:
        return self.area_2d() * 4 + self._base ** 2
