import random

from person import Person


class Husband(Person):

    def eat(self):
        self.satiety += 30
        self.house.fridge_food -= 30

    def play(self):
        self.satiety -= 10
        self.happiness += 20

    def work(self):
        self.satiety -= 10
        self.house.stand_money += 150
        self.house.total_stand_money += 150

    def act(self):
        if self.is_dead:
            print(self.name, 'is dead')
            return 'dead'
        if self.satiety < 30:
            self.eat()
        elif self.house.stand_money < 20:
            self.work()
        else:
            self.play()


class Wife(Person):

    def eat(self):
        self.satiety += 30
        self.house.fridge_food -= 30

    def buy_food(self):
        self.satiety -= 10
        self.house.stand_money -= 20
        self.house.fridge_food += 10
        self.house.cat_food += 10
        self.house.total_fridge_food += 10
        self.house.total_cat_food += 10

    def buy_fur(self):
        self.satiety -= 10
        self.house.stand_money -= 350
        self.house.fur += 1
        self.happiness += 60

    def clean(self):
        self.satiety -= 10
        self.house.mud -= 100

    def act(self):
        if self.is_dead:
            print(self.name, 'is dead')
            return 'dead'
        if self.satiety < 30:
            self.eat()
        elif self.house.fridge_food < 60 or self.house.cat_food < 10:
            self.buy_food()
        elif self.happiness < 30:
            self.buy_fur()
        elif self.house.mud >= 100:
            self.clean()


class Cat(Person):
    def __init__(self, name, house):
        super().__init__(name, house)
        self.happiness = None

    def caress_cat(self):
        pass

    def eat(self):
        self.satiety += 20
        self.house.cat_food -= 10

    def sleep(self):
        self.satiety -= 10

    def scratch(self):
        self.satiety -= 10
        self.house.mud += 5

    def act(self):
        if self.is_dead:
            print(self.name, 'is dead')
            return 'dead'
        if self.satiety < 20:
            self.eat()
        else:
            random.choice([self.sleep(), self.scratch()])
