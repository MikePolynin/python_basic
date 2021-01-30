def sort(input_list):
    for i in range(len(input_list)):
        for index in range(i, len(input_list)):
            if input_list[index] < input_list[i]:
                input_list[index], input_list[i] = input_list[i], input_list[index]


def roller_skates():
    rollers_list = []
    man_list = []
    result = []

    rollers_count = int(input('Кол-во коньков: '))
    for roller in range(rollers_count):
        size = int(input('Размер %i пары: ' % (roller + 1)))
        rollers_list.append(size)

    people_count = int(input('\nКол-во людей: '))
    for man in range(people_count):
        size = int(input('Размер ноги %i человека: ' % (man + 1)))
        man_list.append(size)

    sort(rollers_list)
    sort(man_list)

    for man_size in man_list:
        for roller_size in rollers_list:
            if man_size <= roller_size and rollers_list.index(roller_size) not in result:
                result.append(rollers_list.index(roller_size))
                break

    print('\nНаибольшее кол-во людей, которые могут взять ролики:', len(result))


roller_skates()
