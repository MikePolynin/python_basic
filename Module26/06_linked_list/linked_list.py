class Knot:
    def __init__(self, value: any) -> None:
        self.value = value
        self.next_knot = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __iter__(self):
        self.__current_knot = self.head
        self.__first_knot = True
        return self

    def __next__(self) -> any:
        if self.__first_knot:
            self.__first_knot = False
            return self.__current_knot.value
        while self.__current_knot.next_knot:
            current_value, self.__current_knot = self.__current_knot.next_knot.value, self.__current_knot.next_knot
            return current_value
        raise StopIteration

    def __str__(self) -> str:
        return '[' + ' '.join(str(elem) for elem in self) + ']'

    def append(self, data: any) -> None:
        new_knot = Knot(data)
        if self.head is None:
            self.head = new_knot
        else:
            current_knot = self.head
            while current_knot.next_knot:
                current_knot = current_knot.next_knot
            current_knot.next_knot = new_knot

    def get(self, index: int) -> any:
        __count = 0
        knot_index = index
        current_knot = self.head
        while __count <= knot_index:
            if __count == knot_index:
                return current_knot.value
            __count += 1
            current_knot = current_knot.next_knot

    def remove(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next_knot
        else:
            __count = 0
            knot_index = index - 1
            current_knot = self.head
            while __count <= knot_index:
                if __count == knot_index:
                    current_knot.next_knot = current_knot.next_knot.next_knot
                __count += 1
                current_knot = current_knot.next_knot
