def guess_number():
    max_number = int(input('Введите максимальное число: '))

    numbers_list = [i for i in range(1, max_number + 1)]

    while True:
        numbers = input('\nНужное число есть среди вот этих чисел: ')

        if numbers == 'Помогите!' or numbers == 'помогите':
            print('Артём мог загадать следующие числа: ', end='')
            for i in numbers_list:
                print(i, end=' ')
            break

        else:
            answer = input('Ответ Артёма: ')
            check_list = numbers.split(' ')

            if answer == 'Нет' or answer == 'нет':
                for number in check_list:
                    if int(number) in numbers_list:
                        numbers_list.remove(int(number))
            else:
                first_index = numbers_list.index(int(check_list[0]))
                last_index = numbers_list.index(int(check_list[len(check_list) - 1]))
                numbers_list = numbers_list[first_index:last_index + 1]


guess_number()
