import random

from house import House


def buy_food():
    House.fridge_food += 20
    House.stand_money -= 20


class Man:

    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        self.house = house
        self.is_dead = False

    def eat(self):
        self.house.fridge_food -= 30
        self.satiety += 30

    def work(self):
        self.satiety -= 30
        self.house.stand_money += 30
        self.check_is_dead()

    def play(self):
        self.satiety -= 30
        self.check_is_dead()

    def buy_food(self):
        self.house.fridge_food += 30
        self.house.stand_money -= 30

    def check_is_dead(self):
        if self.satiety < 0:
            self.is_dead = True

    def act(self):
        if self.is_dead:
            print(self.name, 'умер')
            return 'dead'
        number = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.house.fridge_food < 10:
            self.buy_food()
        elif self.house.stand_money < 50:
            self.work()
        elif number == 1:
            self.work()
        elif number == 2:
            self.eat()
        else:
            self.play()
