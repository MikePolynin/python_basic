def pedigree():
    quantity = int(input('Введите количество человек: '))

    tree = dict()

    for i in range(quantity):
        pair = input('{0} пара: '.format(i + 1))

        pair_list = pair.split(' ')

        if i == 0:
            tree[pair_list[1]] = 0

        parent_number = tree[pair_list[1]]
        tree[pair_list[0]] = parent_number + 1

    print('“\nВысота” каждого члена семьи:')
    for key in tree:
        print(key, tree[key])


pedigree()
