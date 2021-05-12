from time import sleep
from typing import Any, Callable
import functools


def slowdown(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print('Ожидание 3 секунды')
        sleep(3)

        result = func(*args, **kwargs)

        return result

    return wrapper()


@slowdown
def test() -> None:
    print('Работа основной функции')
