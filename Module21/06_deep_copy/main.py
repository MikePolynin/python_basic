all_sites = dict()


def make_site(product):
    site = {
        'html': {
            'head': {
                'title': 'Куплю/продам {0} недорого'.format(product)
            },
            'body': {
                'h2': 'У нас самая низкая цена на {0}'.format(product),
                'div': 'Купить',
                'p': 'продать'
            }
        }
    }

    all_sites[product] = site

    print('Сайт для {0}:'.format(product))


def deep_copy():
    quantity = int(input('Сколько сайтов: '))

    for i in range(quantity):
        product = input('\nВведите название продукта для нового сайта: ')

        make_site(product)

        for product in all_sites.keys():
            print('Сайт для {0}:'.format(product))
            print(all_sites[product])


deep_copy()
