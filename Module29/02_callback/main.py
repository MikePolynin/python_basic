import functools
from typing import Callable, Any

app = {}


def callback(route: Any) -> Callable:
    def decorator(func: Callable) -> Callable:
        app[route] = func

        @functools.wraps(func)
        def wrapped_func():
            result = func()
            return result

        return wrapped_func

    return decorator


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')

if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
