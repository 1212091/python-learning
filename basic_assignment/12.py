def is_all_digit_even(n):
    digits = [x for x in str(n) if (int(x) % 2) == 0]
    if len(digits) == len(str(n)):
        return True
    return False


final = filter(is_all_digit_even, list(range(1000, 3001)))

print(final)
