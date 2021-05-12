from typing import Any, Callable
import functools


def debug(func: Callable) -> Callable:
    """
    Декоратор, выводящий название функции, принимаемые параметры и результат выполнения.
    :param func:
    :return:
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print('\nВызывается {}'.format(func.__name__), args, kwargs)

        result = func(*args, **kwargs)

        print("'{0}' вернула значение '{1}'".format(
            func.__name__,
            result))
        print(result)

    return wrapper


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
