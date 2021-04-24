class Person:
    def __init__(self, name, house):
        self.name = name
        self.satiety = 30
        self.happiness = 100
        self.house = house
        self.is_dead = False

    def caress_cat(self):
        self.happiness += 5
        self.satiety -= 10

    def check_is_dead(self):
        if self.satiety < 0:
            self.is_dead = True
        elif self.happiness < 10:
            self.is_dead = True

    def check_mud_level(self):
        if self.house.mud > 90:
            self.happiness -= 10
