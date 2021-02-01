def list_compression():
    list_len = int(input('Введите длину списка: '))
    input_list = [int(input('Введите число: ')) for _ in range(list_len)]

    for _ in range(list_len):
        input_list.append(input_list.pop(input_list.index(0)))

    input_list = input_list[:input_list.index(0)]

    print('\nСписок без "0":', input_list)


list_compression()
