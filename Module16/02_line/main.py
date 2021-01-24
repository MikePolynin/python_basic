def sort(input_list):
    for i in range(len(input_list)):
        for index in range(i, len(input_list)):
            if input_list[index] < input_list[i]:
                input_list[index], input_list[i] = input_list[i], input_list[index]


def class_lists():
    class_1 = list(range(160, 177, 2))
    class_2 = list(range(162, 181, 3))

    class_1.extend(class_2)

    sort(class_1)

    print('Объединенный и отсортированный список:', class_1)


class_lists()
