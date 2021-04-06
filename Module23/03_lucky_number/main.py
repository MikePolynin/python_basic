import random


def lucky_number():
    total_sum = 0
    with open('results.txt', 'w') as results:
        while total_sum < 777:
            try:
                number = input('Введите число: ')
                if not isinstance(number, int):
                    raise TypeError
                total_sum += int(number)
            except TypeError:
                print('Некорректный ввод')
            finally:
                chance = random.randint(0, 13)
                if chance == 13:
                    raise BaseException('Ошибка, данные не будут записаны')
                else:
                    results.write(number + '\n')


lucky_number()
