def rhyme_cnt():
    people = int(input('Кол-во человек: '))
    people_list = list(range(1, people + 1))

    cnt = int(input('Какое число в считалке? '))
    print('Значит, выбывает каждый %i человек' % cnt)

    count_index = 0
    count = people_list[count_index]

    while len(people_list) > 1:
        print('\nТекущий круг людей:', people_list)
        print('Начало счёта с номера', count)

        step = 7 - 7 // len(people_list) * len(people_list)

        out_index = count_index + step - 1
        if out_index >= len(people_list):
            out_index -= out_index // len(people_list) * len(people_list)
        out_number = people_list[out_index]

        print('Выбывает человек под номером', out_number)

        people_list.remove(out_number)

        count_index = out_index
        if count_index >= len(people_list):
            count_index -= count_index // len(people_list) * len(people_list)
        count = people_list[count_index]

    print('\nОстался человек под номером', people_list[0])


rhyme_cnt()
