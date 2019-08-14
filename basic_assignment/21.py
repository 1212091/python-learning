import math
import operator
import sys
from collections import namedtuple

input_data = sys.stdin.readlines()
formatted_input_data = [line.rstrip() for line in input_data]

Pair = namedtuple("Point", ["x_coordinate", "y_coordinate"])

end_position = Pair(0, 0)

for move in formatted_input_data:
    direction, value = move.split(" ")
    if direction == "UP":
        end_position = tuple(map(operator.add, end_position, Pair(int(value), 0)))
    elif direction == "DOWN":
        end_position = tuple(map(operator.add, end_position, Pair(-int(value), 0)))
    elif direction == "LEFT":
        end_position = tuple(map(operator.add, end_position, Pair(0, -int(value))))
    elif direction == "RIGHT":
        end_position = tuple(map(operator.add, end_position, Pair(0, int(value))))

start_position = Pair(0, 0)
distance = int(round(math.sqrt(((end_position[0] - start_position[0])**2) + ((end_position[1] - start_position[1])**2))))

print("Distance: " + str(distance))
