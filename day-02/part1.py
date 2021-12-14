import sys
import numpy as np

mapping = {
    'forward': [1, 0],
    'down': [0, 1],
    'up': [0, -1],
}

pos = [0, 0]
for l in sys.stdin.readlines():
    command, amount = l.strip().split(" ")

    pos = np.add(
        np.dot(
            mapping[command],
            int(amount)
        ),
        pos
    )

print(pos[0] * pos[1])