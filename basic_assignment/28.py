input_list = input()

result = map(int, filter(lambda x: x % 2 == 0, list(input_list)))

print(result)
