def type_logger(func):
    def wrapper(*args):
        for arg in args:
            print(f'{arg}: {type(arg)}')
        res = func(*args)
        return res

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(6))
