from potatogarden import PotatoGarden
from gardener import Gardener


def happy_farm_2():
    my_garden = PotatoGarden(5)
    gardener = Gardener('Bob', my_garden)
    gardener.print_potato_list()
    gardener.cearing()
    gardener.cearing()
    gardener.cearing()
    gardener.get_potato()
    gardener.potatogarden.are_all_ripe()
    gardener.cearing()


happy_farm_2()
