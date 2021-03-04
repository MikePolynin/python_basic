import random


def guess_number():
    max_number = int(input('Введите максимальное число: '))

    numbers_list = {i for i in range(1, max_number + 1)}
    hidden_number = random.randint(1, max_number)

    while True:
        numbers = input('\nНужное число есть среди вот этих чисел: ')

        if numbers == 'Помогите!' or numbers == 'помогите':
            print('Артём мог загадать следующие числа: ', end='')
            for i in numbers_list:
                print(i, end=' ')
            break

        else:
            check_list = numbers.split(' ')

            answer = False
            if str(hidden_number) in check_list:
                answer = True
                print('Ответ Артёма: да')
            else:
                print('Ответ Артёма: нет')

            if not answer:
                for number in check_list:
                    numbers_list.discard(int(number))
            else:
                numbers_list.clear()
                numbers_list = {int(i) for i in check_list}


guess_number()
