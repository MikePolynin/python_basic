class Warrior:

    def __init__(self, index):
        self.index = index
        self.health = 100

    def fighting(self, warrior):
        self.health -= 20

        print('\nАтаковал воин {}'.format(warrior.index))
        print('Здоровье война {}: {}'.format(self.index, self.health))

        if self.health == 0:
            print('\nПобедил воин {}'.format(warrior.index))

            return False

        return True
