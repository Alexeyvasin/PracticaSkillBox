import os.path
from collections.abc import Iterator
from contextlib import contextmanager


@contextmanager
def in_dir(dir_path) -> Iterator:
    cur_path = os.getcwd()
    try:
        try:
            os.chdir(dir_path)
        except FileNotFoundError as exc:
            print(exc)
        yield
    except (FileNotFoundError, ZeroDivisionError) as exc:
        print(exc)
    finally:
        os.chdir(cur_path)


with in_dir('/home/alexey'):
    print(os.listdir())
    10 / 0
