from functools import reduce
from typing import List

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]


def new_lists():
    new_list_1 = map(lambda elem: round(elem ** 3, 3), floats)

    print('Числа из списка floats, возведенные в 3 степень и округленные до 3 символов после запятой')
    for elem in new_list_1:
        print(elem)

    new_list_2 = filter(lambda elem: len(elem) >= 5, names)

    print('\nИмена из списка names, из 5 и более букв')
    for elem in new_list_2:
        print(elem)

    new_list_3 = reduce(lambda elem, sum: sum * elem, numbers)

    print('\nПроизведение элементов из списка names\n{}'.format(new_list_3))


if __name__ == '__main__':
    new_lists()
