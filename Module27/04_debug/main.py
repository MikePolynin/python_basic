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

        def stringify_arg(arg: Any) -> str:
            if isinstance(arg, str):
                return '"{0}"'.format(arg)
            else:
                return str(arg)

        args_str = [stringify_arg(a) for a in args]
        kwargs_str = ['{0}={1}'.format(k, stringify_arg(v)) for k, v in kwargs.items()]

        params = ', '.join(args_str + kwargs_str)

        print('\nВызывается {}'.format(func.__name__) + '(' + params + ')')

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
