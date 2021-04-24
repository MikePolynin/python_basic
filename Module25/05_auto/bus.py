from automobile import Automobile


class Bus(Automobile):
    def __init__(self, coordinates, corner):
        super().__init__(coordinates, corner)
        self.passengers = 0
        self.money = 0

    def get_in(self, count):
        self.passengers += count

    def get_out(self, count):
        self.passengers -= count

    def move(self, distance):
        super().move(distance)
        self.money += 5 * self.passengers * distance
