import sys

input_data = sys.stdin.readlines()
formatted_input_data = [line.rstrip().upper() for line in input_data]

print(formatted_input_data)
