import random

from house import House

from man import Man


def cohabitation():
    house = House
    people = [Man('Борис', house), Man('Андрей', house)]
    live_man = people

    day = 1
    while day < 366:
        if len(live_man) > 0:
            print('Наступил {} день'.format(day))
            for man in live_man:
                if man.is_dead:
                    print(man.name, 'умер')
                    live_man.remove(man)
                number = random.randint(1, 6)
                if man.satiety < 20:
                    man.eat()
                elif man.house.fridge_food < 10:
                    man.buy_food()
                elif man.house.stand_money < 50:
                    man.work()
                elif number == 1:
                    man.work()
                elif number == 2:
                    man.eat()
                else:
                    man.play()
            if day == 365:
                print('Прошел год. Выжившие:')
                for man in live_man:
                    print(man.name)
        day += 1


cohabitation()
