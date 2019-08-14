import itertools

first_file = open('42.txt', "r")
second_file = open('43.txt', "r")

first_file_lines = first_file.readlines()

second_file_lines = second_file.readlines()

first_file_lines = [line.rstrip() for line in first_file_lines]
second_file_lines = [line.rstrip() for line in second_file_lines]


combined = [x + " " + y for x in first_file_lines for y in second_file_lines]

print(combined)
