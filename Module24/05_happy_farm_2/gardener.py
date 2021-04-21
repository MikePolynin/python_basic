from potatogarden import PotatoGarden


class Gardener:
    def __init__(self, name='', potatogarden=PotatoGarden):
        self.name = name
        self.potatogarden = potatogarden
        self.potato_list = 0

    def cearing(self):
        self.potatogarden.grow_all()

    def print_potato_list(self):
        print('\nЗапасы картошки: {}'.format(self.potato_list))

    def get_potato(self):
        self.potato_list += self.potatogarden.give_potatoes()
        self.print_potato_list()
        self.potatogarden.__init__(self.potatogarden.give_potatoes())

