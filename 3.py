input_number = input()

keys = list(range(1, int(input_number) + 1))
values = [x * x for x in keys]
result = dict(zip(keys, values))

print("Result: " + str(result))
