import sys
import numpy as np

vector = np.array([list(l.strip()) for l in sys.stdin.readlines()]).astype(int)

gamma = 0
epsilon = 0
for b in np.apply_along_axis(lambda x: round(sum(x) / x.shape[0]), 0, vector):
    gamma = (gamma << 1) | b
    epsilon = (epsilon << 1) | (b^1)

print(gamma * epsilon)