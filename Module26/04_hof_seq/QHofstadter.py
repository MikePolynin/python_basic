class QHofstadter:
    def __init__(self, numbers_list):
        self.numbers_list = numbers_list

    def __iter__(self):
        return self

    def __next__(self):
        if self.numbers_list[0] != 1 or self.numbers_list[1] != 1:
            raise Exception('Wrong input numbers')
        else:
            elem = self.numbers_list[-self.numbers_list[-1]] + self.numbers_list[-self.numbers_list[-2]]
            self.numbers_list.append(elem)
            return elem
