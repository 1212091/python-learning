input_number = input()


def return_even_number(n):
    i = 0
    while i <= n:
        yield i
        i += 2


number_gen = return_even_number(int(input_number))

print(list(number_gen))
