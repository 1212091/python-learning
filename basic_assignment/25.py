def generate_dict():
    num_dict = dict((x, x ** 2) for x in list(range(1, 21)))
    for _, value in num_dict.items():
        print(str(value))


generate_dict()
