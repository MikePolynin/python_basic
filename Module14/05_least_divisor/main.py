def divisor_find():
    n = int(input('Введите число: '))

    for divisor in range(2, n):
        if n % divisor == 0:
            break

    print('\nНаименьший делитель, отличный от единицы:', divisor)


divisor_find()
