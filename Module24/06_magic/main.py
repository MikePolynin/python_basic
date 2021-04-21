from water import Water
from air import Air
from fire import Fire
from ground import Ground
from life import Life


def magic():
    print(Water() + Air())
    print(Air() + Fire())
    print(Fire() + Ground())
    print(Air() + Life())


magic()
