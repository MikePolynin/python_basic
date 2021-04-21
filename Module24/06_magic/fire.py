from ground import Ground
from lava import Lava
from life import Life
from firebird import Firebird


class Fire:

    def __str__(self):
        return 'Fire'

    def __add__(self, other):
        if isinstance(other, Ground):
            return Lava()
        elif isinstance(other, Life):
            return Firebird()
        else:
            return None
