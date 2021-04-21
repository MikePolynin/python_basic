from life import Life
from plant import Plant


class Ground:

    def __str__(self):
        return 'Ground'

    def __add__(self, other):
        if isinstance(other, Life):
            return Plant()
        else:
            return None
