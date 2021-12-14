import sys
import numpy as np

class Position:
    horizontal: int
    depth: int

    def __init__(self, horizontal: int = 0, depth: int = 0):
        self.horizontal = horizontal
        self.depth = depth

    def add(self, distance: int, aim: int):
        self.horizontal += distance
        self.depth += aim * distance

aim = 0
pos = Position()
for l in sys.stdin.readlines():
    command, distance = l.strip().split(" ")
    distance = int(distance)

    if command == "forward":
        pos.add(distance, aim)
    elif command == "down":
        aim += distance
    elif command == "up":
        aim -= distance


print(pos.horizontal * pos.depth)