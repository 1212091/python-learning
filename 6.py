import math

input_data = input()

input_list = [int(x) for x in input_data]

result = [int(round(math.sqrt(((i * 50 * 2) / 30)))) for i in input_list]

print(result)
