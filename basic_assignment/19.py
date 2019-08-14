import operator
import sys

input_data = sys.stdin.readlines()
formatted_input_data = [line.rstrip() for line in input_data]
person_tuple_list = [tuple(person.split(",")) for person in formatted_input_data]
person_tuple_list.sort(key=operator.itemgetter(0, 1, 2))

print(person_tuple_list)


