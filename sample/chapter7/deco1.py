import functools


def deco(f):
    @functools.wraps(f)
    def wrapper(*x, **y):
        print('BEGIN!')
        f(*x, **y)
        print('END!')
    return wrapper


@deco
def hello():
    print('hello')


hello()
