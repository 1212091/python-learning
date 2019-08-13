def is_divisible_by_seven(x):
    if x % 7 == 0:
        return True
    return False


def is_not_multiple_of_five(x):
    while x > 0:
        x -= 5
    if x == 0:
        return False
    return True


result = [x for x in range(2000, 3201) if is_divisible_by_seven(x) and is_not_multiple_of_five(x)]
print(result)
