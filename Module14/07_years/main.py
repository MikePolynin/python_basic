def check(year):
    str_year = str(year)
    for n in range(3):
        count = 1
        for m in range(n + 1, 4, 1):
            if str_year[n] == str_year[m]:
                count += 1
        if count >= 3:
            return True


def years():
    first_year = int(input('Введите первый год: '))
    second_year = int(input('Введите второй год: '))

    print('\nГода от', first_year, 'до', second_year, 'с тремя одинаковыми цифрами:')

    for year in range(first_year, second_year, 1):
        if check(year):
            print(year)


years()
