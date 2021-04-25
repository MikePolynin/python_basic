from house import House
from family import Husband, Wife, Cat, Child


def cohabitation_2():
    house = House
    family = [Husband('Борис', house), Wife('Анна', house),
              Cat('Барсик', house), Cat('Мурзик', house), Cat('Васька', house),
              Child('Малой', house)]
    alives = family

    day = 1
    while day < 366:
        house.mud += 5
        if len(alives) > 0:
            print('Наступил {} день'.format(day))
            for unit in alives:
                unit.check_mud_level()
                if unit.act() == 'dead':
                    alives.remove(unit)
            if day == 365:
                print('Прошел год. Выжившие:')
                for unit in alives:
                    print(unit.name)
                print('За год заработано {}\nкуплено шуб {}\nкуплено еды {}\nкуплено кошачьей еды {}'.format(
                    house.total_stand_money,
                    house.fur,
                    house.total_fridge_food,
                    house.total_cat_food))
        day += 1


cohabitation_2()
