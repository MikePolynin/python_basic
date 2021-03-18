nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def list_of_lists_2(user_list, result_list=None):
    if result_list is None:
        result_list = list()

    for i in range(len(user_list)):
        if isinstance(user_list[i], list):
            list_of_lists_2(user_list[i], result_list)
        else:
            result_list.append(user_list[i])

    return result_list


print('Ответ:', list_of_lists_2(nice_list))
