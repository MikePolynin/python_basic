def restaurant_menu():
    dishes = 'утиное филе;фланк-стейк;банановый пирог;плов'

    print('Доступное меню: {}'.format(dishes))
    print('На данный момент в меню есть: {}'.format(', '.join(dishes.split(';'))))


restaurant_menu()
