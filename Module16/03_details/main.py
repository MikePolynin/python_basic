def shop_func():
    shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
            ['педаль', 100], ['седло', 1500], ['рама', 12000],
            ['обод', 2000], ['шатун', 200], ['седло', 2700]]
    count = 0
    cost = 0

    user_choice = input('Название детали: ')

    for product in shop:
        if product[0] == user_choice:
            count += 1
            cost += product[1]

    print('Кол-во деталей -', count)
    print('Общая стоимость -', cost)


shop_func()
