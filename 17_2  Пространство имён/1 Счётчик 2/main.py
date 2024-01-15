def counter(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(count)
        return func(*args, **kwargs)

    return wrapper


@counter
def foo():
    pass


foo()
foo()


@counter
def foo2():
    pass


foo2()
foo()
foo()
foo2()
