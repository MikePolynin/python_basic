from typing import Any, Callable
import functools


def counter(func: Callable) -> Callable:
    """
    Декоратор, считающий количество вызовов функции.
    :param func:
    :return:
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@counter
def greeting(name: str, age: int = None) -> str:
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
print('Вызов №{}'.format(greeting.count))

greeting("Миша", age=100)
print('Вызов №{}'.format(greeting.count))

greeting(name="Катя", age=16)
print('Вызов №{}'.format(greeting.count))
