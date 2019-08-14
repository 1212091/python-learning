def logged(func):
    def wrapper(*args, **kwargs):
        print("You called {0} {1} {2}".format(func.__name__, args, kwargs))
        result = func(*args, **kwargs)
        print("it returned %d" % result)
        return result
    return wrapper


@logged
def sum_arg(*args, **kwargs):
    return 3 + len(args) + len(kwargs)


result_sum = sum_arg(4, x=4, y=4)
print(result_sum)
