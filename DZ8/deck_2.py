def val_checker(valid):
    def wrapper(func):
        def validator(*args):
            if valid(*args):
                res = func(*args)
                return res
            else:
                raise ValueError(f'Incorrect value: {args}')

        return validator
    return wrapper


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
print(calc_cube(-5))
