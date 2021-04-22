class Player:
    x_o = set()

    def __init__(self, name):
        self.name = name

    def move(self, elems, x_o):
        while True:
            cell = input('\nКуда поставить {}? '.format(x_o))
            if not cell.isdigit():
                print('Некорректный ввод')
            elif 0 >= int(cell) or int(cell) > 9:
                print('Некорректный ввод')
            elif isinstance(elems[int(cell) - 1], str):
                print('Некорректный ввод')
            else:
                elems[int(cell) - 1] = x_o
                self.x_o.add(int(cell))
                break
