input_data = raw_input(">")


def divisible_by_five(binary_number):
    decimal_number = int(binary_number, 2)
    if (decimal_number % 5) == 0:
        return True
    return False


binary_list = input_data.split(",")
result = filter(divisible_by_five, binary_list)
print(result)
