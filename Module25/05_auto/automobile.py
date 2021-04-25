import math


class Automobile:
    def __init__(self, coordinates, corner):
        self.coordinates = coordinates
        self.corner = corner

    def move(self, distance):
        self.coordinates[0] *= distance
        self.coordinates[1] *= distance

    def turn(self, corner):
        self.coordinates[0] = round(self.coordinates[0] * math.cos(corner) - self.coordinates[1] * math.sin(corner), 3)
        self.coordinates[1] = round(self.coordinates[1] * math.cos(corner) + self.coordinates[0] * math.sin(corner), 3)
