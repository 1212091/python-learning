def memoize(function):
    memo = {}

    def wrapper(*args):
        if args in memo:
            print("Get from cache")
            return memo[args]
        else:
            print("Push new value to cache")
            result = function(*args)
            memo[args] = result
            return result

    return wrapper


@memoize
def fibonacci(n):
    assert n >= 0
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


final_result = fibonacci(7)
print(str(final_result))
