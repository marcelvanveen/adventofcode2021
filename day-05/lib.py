from dataclasses import dataclass
import sys
import enum

@dataclass
class Coordinate:
    x: int
    y: int

class Direction(enum.Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"
    DIAGONAL = "diagonal"

@dataclass
class Vent:
    begin: Coordinate
    end: Coordinate
    direction: Direction

    def __init__(self, begin: Coordinate, end: Coordinate):
        self.begin = begin
        self.end = end

        if self.begin.x == self.end.x:
            self.direction = Direction.VERTICAL
        elif self.begin.y == self.end.y:
            self.direction = Direction.HORIZONTAL
        else:
            self.direction = Direction.DIAGONAL

    def get_range(self, begin, end):
        if begin < end:
            return range(begin, end + 1, 1)
        else:
            return range(begin, end - 1, -1)

    def get_coordinates(self):
        match self.direction:
            case Direction.HORIZONTAL:
                for x in self.get_range(self.begin.x, self.end.x):
                    yield Coordinate(x, self.begin.y)

            case Direction.VERTICAL:
                for y in self.get_range(self.begin.y, self.end.y):
                    yield Coordinate(self.begin.x, y)

            case Direction.DIAGONAL:
                for x, y in zip(
                    self.get_range(self.begin.x, self.end.x),
                    self.get_range(self.begin.y, self.end.y)
                ):
                    yield Coordinate(x, y)



def create_field(vents):
    max_x = 0
    max_y = 0

    for v in vents:
        max_x = max(max_x, v.begin.x, v.end.x)
        max_y = max(max_y, v.begin.y, v.end.y)

    return [[0] * (max_x+1) for i in range(max_y+1)]

def display_field(field):
    for y in field:
        for x in y:
            print(str(x) if x > 0 else '.', end='')
        print('')

def read_vents():
    vents = []
    for line in sys.stdin.readlines():
        vents.append(
            Vent(
                *[Coordinate(int(c[0]), int(c[1])) for c in [p.split(",") for p in line.strip().split(" -> ")]]
            )
        )
    return vents