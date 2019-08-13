input_data = input()

input_number = int(input_data)

number_list = [x * input_number for x in [1, 11, 111, 1111]]

print(sum(number_list))
