import functools
from collections.abc import Callable
from typing import Optional


def check_permission(_func: Optional[Callable] = None, *, role: str = '') -> Callable:
    def permission(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            if role in user_permissions:
                result = func(*args, **kwargs)
                return result
            raise PermissionError('У пользователя недостаточно прав, чтобы выполнить функцию {}'.format
                                  (func.__name__))

        return wrapped_func()

    if _func is None:
        return permission
    return permission(_func)


user_permissions = ['admin']


@check_permission(role='admin')
def delete_site():
    print('Удаляем сайт')


@check_permission(role='user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
