from typing import Callable
from functools import wraps
from datetime import datetime


def create_time(cls) -> Callable:
    """
    Декоратор выводит на экран время создания экземпляра класса и список всех методов класса
    :param cls: cls
    :return: Callable
    """
    @wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print(datetime.now())
        for name in dir(cls):
            attr = getattr(cls, name)
            str_type = str(type(attr))
            if 'function' in str_type or 'method' in str_type:
                print(f'{str_type}: {name}')
        return instance

    return wrapper


@create_time
class MyClass:
    a = 10

    @classmethod
    def method1(cls):
        print("I am method1")
        pass

    def method2(self):
        print(self.a)


my_class = MyClass()
