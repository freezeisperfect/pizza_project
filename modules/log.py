from random import randint
from typing import Callable, Any


def log(print_template: str) -> Callable:
    """
    Создание декоратора для логирования событий.

    Parameters
    ----------
    print_template: str
        Шаблон для вывода лога события.

    Returns
    -------
    Callable
        Декорированная функция.
    """
    def decorator(func: Callable) -> Callable:
        def log_wrapper(*args: Any, **kwargs: Any):
            result = func(*args, **kwargs)
            print(print_template.format(randint(1, 10)))
            return result
        return log_wrapper
    return decorator
