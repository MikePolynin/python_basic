import datetime
from typing import Any, Callable
import functools

exp_list = []


def logging(func: Callable) -> Callable:
    """
    Декоратор, выводящий название функции и ее документацию.
    При возникновении ошибки записывает в файл function_errors.log название функции, ошибку и дату возникновения.
    :param func:
    :return:
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        global exp_list

        print('Название функции: {}'.format(func.__name__))
        print(func.__doc__)

        try:
            return func(*args, **kwargs)
        except Exception as exp:
            print(exp)
            exp_list.append('В функции {0} произошла ошибка {1} в {2}'.format(
                func.__name__,
                exp,
                datetime.datetime.now()
            ))

        with open('function_errors.log', 'w', encoding='utf8') as log_file:
            for line in exp_list:
                log_file.write(line + '\n')

    return wrapper()


@logging
def degree() -> int:
    """
    Функция вычисления суммы 25 степеней чисел от 0 до 5
    :return: int
    """
    result = 0

    for num in range(5):
        result += num ** 25

    return result


@logging
def list_error() -> Exception:
    """
    Функция выдает ошибку list index out of range
    :return:
    """
    my_list = [_ for _ in range(5)]

    return my_list[10]


@logging
def degree() -> int:
    """
    Функция вычисления суммы квадратов чисел от 0 до 150
    :return: int
    """
    result = 0

    for num in range(150):
        result += num ** 2

    return result


@logging
def list_error() -> Exception:
    """
    Функция выдает ошибку division by zero
    :return:
    """
    result = 5 / 0

    return result
