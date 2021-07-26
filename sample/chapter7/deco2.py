import functools


def comment(f):
    @functools.wraps(f)
    def wrapper(*x, **y):
        print('<!--')
        f(*x, **y)
        print('-->')
    return wrapper


@comment
def hello():
    print('hello')


hello()
