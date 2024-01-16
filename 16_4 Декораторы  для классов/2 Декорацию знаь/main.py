import functools
from collections.abc import Callable


def logging(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Декоратор',func.__name__)
        res = func(*args, **kwargs)
        return res

    return wrapper


def decor_methods(decorator: Callable) -> Callable:
    @functools.wraps(decorator)
    def wrapper(cls):
        for name in dir(cls):
            if not name.startswith('__') and not name.endswith('__'):
                method = getattr(cls, name)
                setattr(cls, name, decorator(method))
        print(dir(cls))
        return cls
    return wrapper
@decor_methods(logging)
class A:

    def __init__(self):
        self.a = 0

    def method1(self):
        print('I - method1', self.a)

a = A()

a.method1()

print('Hello')