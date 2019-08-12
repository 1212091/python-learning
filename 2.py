from functools import reduce

input_number = input()


def factorial(x1, x2): return x1 * x2


result = reduce(factorial, list(range(1, int(input_number + 1))))
print("Result: " + str(result))