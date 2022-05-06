def type_logger(my_function):
    def my_func(*args):
        calc = my_function(*args)
        if len(args) == 1:
            print(f'{args[0]}:{type(args[0])}')
        else:
            for i in args:
                print(f'{i}:{type(i)}')
        return calc

    return my_func

@type_logger
def calc_cube(x):
    return x ** 3
print(calc_cube(5))