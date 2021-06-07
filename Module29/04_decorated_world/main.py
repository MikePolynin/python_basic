from collections.abc import Callable


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    def decorator_wrap(func, *args, **kwargs):
        print('Переданные арги и кварги в декоратор: {} {}'.format(args, kwargs))
        result = decorator(func, *args, **kwargs)
        return result

    return decorator_wrap


@decorator_with_args_for_any_decorator
def decorated_decorator(*args_decorator, **kwargs_decorator) -> Callable:
    def decorator(func: Callable):
        def wrap(*args, **kwargs):
            result = func(*args, **kwargs)
            return result

        return wrap

    return decorator


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
