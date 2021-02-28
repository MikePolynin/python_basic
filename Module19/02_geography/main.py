def geography():
    countries = dict()

    quantity = int(input('Кол-во стран: '))

    for i in range(quantity):
        country = input('{0} страна: '.format(i + 1))

        country_list = country.split(' ')
        countries[country_list[0]] = country_list[1:]

    for i in range(3):
        count = 0
        town = input('\n{0} город: '.format(i + 1))
        for key in countries:
            count += 1
            if town in countries[key]:
                print('Город {0} расположен в стране {1}.'.format(town, key))
                break
            if count == len(countries.keys()):
                print('По городу {0} данных нет.'.format(town))


geography()
