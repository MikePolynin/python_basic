from warrior import Warrior
import random


def fight():
    units = [Warrior(index) for index in range(2)]

    while True:
        index = random.randint(0, 1)

        if not Warrior.fighting(units[1 - index], units[index]):
            break


fight()
