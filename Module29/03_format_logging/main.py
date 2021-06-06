import functools
import time
from typing import Callable


def log(time_format: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def decorated_func(*args, **kwargs):
            print("- Запускается '{}'. Дата и время запуска: {} ".format(
                func.__name__,
                time.strftime(time_format)
            ))
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print("- Завершение '{}', время работы = {}с ".format(
                func.__name__,
                round(end_time - start_time, 3)
            ))
            return result

        decorated_func.__name__ = func.__name__
        return decorated_func

    return decorator


def log_methods(decorator: Callable) -> Callable:
    @functools.wraps(decorator)
    def wrap(cls):
        for method_name in dir(cls):
            if not method_name.startswith('__'):
                current_method = getattr(cls, method_name)
                wrapped_method = decorator(current_method)
                setattr(cls, method_name, wrapped_method)
        return cls

    return wrap


@log_methods(log("b d Y - H:M:S"))
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods(log("b d Y - H:M:S"))
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Тут метод test sum 1 у наследника")

    def test_sum_2(self):
        print("Тут метод test sum 2 у наследника")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
