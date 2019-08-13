input_data = input()
input_list = [int(x) for x in input_data]

matrix = [[(x * y) for x in range(input_list[1])] for y in range(input_list[0])]

print(matrix)
