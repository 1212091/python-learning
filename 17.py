import sys

input_data = sys.stdin.readlines()
formatted_input_data = [line.rstrip() for line in input_data]

result = 0
for item in formatted_input_data:
    key, value = item.split(" ")
    if key == 'D':
        result = result + int(value)
    elif key == 'W':
        result = result - int(value)


print(result)
