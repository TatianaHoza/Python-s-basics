def val_checker(callback):
    def my_func(func):
        def wrapper(*args):
            for x in args:
                if not callback(x):
                    raise ValueError(f'wrong val: {x}')
            return func(*args)

        return wrapper

    return my_func


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

print(calc_cube(5))
#print(calc_cube(-5))