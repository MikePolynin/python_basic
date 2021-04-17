from fire import Fire
from ground import Ground
from lighting import Lightning
from dust import Dust
from life import Life
from bird import Bird


class Air:
    def __str__(self):
        return 'Air'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Ground):
            return Dust()
        elif isinstance(other, Life):
            return Bird()
        else:
            return None
