import collections


# def can_be_poly(string: str) -> bool:
#     dict_1 = {}
#     dict_2 = {}
#     is_poly = True
#
#     for i in range(len(string)):
#         dict_1[i] = string[i]
#         dict_2[len(string) - 1 - i] = string[i]
#
#     ordered_dict_1 = collections.OrderedDict(dict_1)
#     ordered_dict_2 = collections.OrderedDict(dict_2)
#
#     for i in range(len(string)):
#         if ordered_dict_1.get(i) == ordered_dict_2.get(i):
#             continue
#         else:
#             is_poly = False
#
#     return is_poly


def check_is_palindrome(string: str) -> bool:
    is_poly = True

    for i in range(int(len(string) / 2)):
        if string[i] != string[len(string) - 1 - i]:
            is_poly = False
            break

    return is_poly


def can_be_poly(string: str) -> bool:
    counter = collections.Counter()
    odd_counter = 0
    odd_symbol = []

    for elem in string:
        counter[elem] += 1

    for symbol, quantity in counter.items():
        if quantity % 2 == 1:
            odd_counter += 1
            odd_symbol.append(symbol)

    if odd_counter > 1:
        is_poly = False
    else:
        if odd_counter == 1:
            middle = int((len(string) - 1) / 2)
            if len(string) % 2 != 1 or odd_symbol[0] != string[middle]:
                is_poly = False
            else:
                string_for_check = string[:middle] + string[middle + 1:]
                is_poly = check_is_palindrome(string_for_check)
        elif odd_counter == 0 and len(string) % 2 == 1:
            is_poly = False
        else:
            is_poly = check_is_palindrome(string)

    return is_poly


if __name__ == '__main__':
    print(can_be_poly('ababa'))
    print(can_be_poly('abbbc'))
