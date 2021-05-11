from typing import Any, Callable
import functools


def how_are_you(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')

        result = func(*args, **kwargs)

        return result

    return wrapper()


@how_are_you
def test() -> None:
    print('Работа основной функции')

