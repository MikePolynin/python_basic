from tax import Apartment, Car, CountryHouse


def taxes():
    money = float(input('Сколько у вас денег? '))
    worth = float(input('Какова стоимость вашего имущества? '))

    apartment = Apartment(worth, 'my_home')
    car = Car(worth, 'my_car')
    country_house = CountryHouse(worth, 'my_country_house')

    apartment_tax = apartment.count_tax()
    car_tax = car.count_tax()
    country_house_tax = country_house.count_tax()
    sum_tax = apartment_tax + car_tax + country_house_tax

    print('\nНалог на квартиру =', apartment_tax)
    print('Налог на машину =', car_tax)
    print('Налог на загородный дом =', country_house_tax)

    print('\nОбщая сумма налогов {} рублей'.format(apartment_tax + car_tax + country_house_tax))

    if sum_tax > money:
        print('На налоги не хватает {} рублей'.format(sum_tax - money))


taxes()
