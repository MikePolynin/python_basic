from typing import List

strings: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]


def zip_again():
    results = map(lambda x, y: (x, y), strings, numbers)

    for elem in results:
        print(elem)


if __name__ == '__main__':
    zip_again()
