def pizza():
    quantity = int(input('Введите кол-во заказов: '))

    orders_dict = dict()

    for i in range(quantity):
        order = input('{0} заказ: '.format(i + 1))

        order_list = order.split(' ')

        if order_list[0] in orders_dict:
            if order_list[1] in orders_dict[order_list[0]]:
                orders_dict[order_list[0]][order_list[1]] = orders_dict[order_list[0]].pop(order_list[1]) + \
                                                            int(order_list[2])
            else:
                orders_dict[order_list[0]][order_list[1]] = int(order_list[2])
        else:
            orders_dict[order_list[0]] = {order_list[1]: int(order_list[2])}

    print()
    for name in orders_dict:
        print(name, ':')
        for order in orders_dict[name]:
            print('     ', order, ':', orders_dict[name][order])


pizza()
