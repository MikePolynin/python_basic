list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


# can_continue = True
# for x in list_1:
#     for y in list_2:
#         result = x * y
#         print(x, y, result)
#         if result == to_find:
#             print('Found!!!')
#             can_continue = False
#             break
#     if not can_continue:
#         break


def get_pair(list1, list2):
    for x in list1:
        for y in list2:
            res = x * y
            if res <= to_find:
                res_str = '{0} {1} {2}'.format(x, y, res)
                yield res_str
                if res == to_find:
                    print('Found!!!')
                    return
            else:
                return


for result in get_pair(list_1, list_2):
    print(result)
