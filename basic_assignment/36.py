input_value = input()


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print("Value of fibonacci is: " + str(fib(int(input_value))))
