from potato import Potato


class PotatoGarden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('\nКартошка растет')
        for potato in self.potatoes:
            potato.grow()

    def are_all_ripe(self):
        if not all([potato.is_ripe() for potato in self.potatoes]):
            print('\nКартошка еще не созрела')
        else:
            print('\nКартошка созрела')

    def give_potatoes(self):
        return len(self.potatoes)
