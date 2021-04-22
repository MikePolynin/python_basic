class Game:
    elems = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def print_field(self):
        print()
        count = 0
        for line in range(3):
            for elem in range(3):
                print('{:^4}'.format(self.elems[count]), end='')
                count += 1
            print()

    def playing(self):
        self.print_field()

        while True:
            self.player_1.move(self.elems, 'X')
            self.print_field()
            if self.check_end(self.player_1):
                break
            self.player_2.move(self.elems, 'O')
            self.print_field()
            if self.check_end(self.player_2):
                break

    def check_end(self, player):
        winner_set = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
        for win_set in winner_set:
            if win_set <= player.x_o:
                print('\nПобеда {}'.format(player.name))
                return True
        if len(self.player_1.x_o) + len(self.player_2.x_o) == 9:
            print('\nХодов больше нет')
            return True
        return False
