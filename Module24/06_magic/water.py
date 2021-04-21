from air import Air
from fire import Fire
from ground import Ground
from storm import Storm
from vapor import Vapor
from mud import Mud
from life import Life
from fish import Fish


class Water:
    def __str__(self):
        return 'Water'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Ground):
            return Mud()
        elif isinstance(other, Life):
            return Fish()
        else:
            return None
