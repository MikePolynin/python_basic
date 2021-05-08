from collections import Iterable


class Iterator:
    def __init__(self, max_int: int) -> None:
        self.max_int = max_int
        self.__count = 0

    def __iter__(self) -> Iterable:
        return self

    def __next__(self) -> int:
        if self.__count < self.max_int:
            self.__count += 1
            return self.__count ** 2
        raise StopIteration


def generator(max_int: int) -> int:
    for number in range(1, max_int + 1):
        yield number ** 2
