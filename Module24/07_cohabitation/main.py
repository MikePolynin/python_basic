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
                if man.act() == 'dead':
                    live_man.remove(man)
            if day == 365:
                print('Прошел год. Выжившие:')
                for man in live_man:
                    print(man.name)
        day += 1


cohabitation()
