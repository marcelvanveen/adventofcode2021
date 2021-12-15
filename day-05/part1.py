from lib import create_field, read_vents, display_field, Direction
import itertools

vents = read_vents()
field = create_field(vents)

for v in vents:
    if v.direction != Direction.DIAGONAL:
        for c in v.get_coordinates():
            field[c.y][c.x] += 1

print(sum([1 for v in itertools.chain.from_iterable(field) if v > 1]))