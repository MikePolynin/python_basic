import math


class Circle:
    def __init__(self, center_x=0, center_y=0, radius=1):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def find_square(self):
        square = math.pi * self.radius ** 2
        return round(square, 2)

    def find_perimeter(self):
        perimeter = math.pi * self.radius * 2
        return round(perimeter, 2)

    def grow(self, times):
        if isinstance(times, int) or isinstance(times, float):
            self.radius *= times
        return round(self.radius, 2)

    def crossing(self, circle):
        distance = ((abs(self.center_x - circle.center_x)) ** 2 + (abs(self.center_y - circle.center_y)) ** 2) ** 0.5
        if distance < self.radius + circle.radius:
            return True
        return False
