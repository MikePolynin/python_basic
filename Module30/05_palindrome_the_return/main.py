import collections


def can_be_poly(string: str) -> bool:
    dict_1 = {}
    dict_2 = {}
    is_poly = True

    for i in range(len(string)):
        dict_1[i] = string[i]
        dict_2[len(string) - 1 - i] = string[i]

    ordered_dict_1 = collections.OrderedDict(dict_1)
    ordered_dict_2 = collections.OrderedDict(dict_2)

    for i in range(len(string)):
        if ordered_dict_1.get(i) == ordered_dict_2.get(i):
            continue
        else:
            is_poly = False

    return is_poly


if __name__ == '__main__':
    print(can_be_poly('ababa'))
    print(can_be_poly('abbbc'))
