def goods_store():
    goods = {
        'Лампа': '12345',
        'Стол': '23456',
        'Диван': '34567',
        'Стул': '45678',
    }

    store = {
        '12345': [
            {'quantity': 27, 'price': 42},
        ],
        '23456': [
            {'quantity': 22, 'price': 510},
            {'quantity': 32, 'price': 520},
        ],
        '34567': [
            {'quantity': 2, 'price': 1200},
            {'quantity': 1, 'price': 1150},
        ],
        '45678': [
            {'quantity': 50, 'price': 100},
            {'quantity': 12, 'price': 95},
            {'quantity': 43, 'price': 97},
        ],
    }

    for key in goods:
        total_quantity = 0
        total_price = 0

        for i in range(len(store[goods[key]])):
            total_quantity += store[goods[key]][i]['quantity']
            total_price += store[goods[key]][i]['quantity'] * store[goods[key]][i]['price']

        print('\n{0} - {1} шт, стоимость {2} руб'.format(
            key,
            total_quantity,
            total_price))


goods_store()
