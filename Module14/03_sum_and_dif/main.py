def sum_count(n):
    summ = 0

    while n >= 0.1:
        summ += n % 10
        n //= 10

    return summ


def digits_count(n):
    digits = 0

    while n >= 0.1:
        digits += 1
        n //= 10

    return digits


def sum_and_dif():
    n = int(input('Введите число: '))

    summ = sum_count(n)
    digits = digits_count(n)

    print('\nСумма чисел:', summ)
    print('Кол-во цифр в числе:', digits)
    print('Разность суммы и кол-ва цифр:', summ - digits)


sum_and_dif()
