def lucky_number():
    total_sum = 0
    numbers = list()
    while total_sum < 777:
        try:
            number = input('Введите число: ')
            if number.isalpha():
                raise TypeError
            total_sum += int(number)
            numbers.append(number + '\n')
        except TypeError:
            print('Некорректный ввод')
        finally:
            with open('results.txt', 'w') as results:
                for num in numbers:
                    results.write(num)


lucky_number()
