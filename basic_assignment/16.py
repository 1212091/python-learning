input_data = raw_input(">")

number_list = input_data.split(",")


def is_odd_number(number):
    if (int(number) % 2) != 0:
        return True
    return False


result = map(int, filter(is_odd_number, number_list))

print(result)
