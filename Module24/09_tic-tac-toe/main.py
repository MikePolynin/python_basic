from player import Player
from game import Game

player_1 = Player('Boris')
player_2 = Player('Maksim')

my_game = Game(player_1, player_2).playing()
