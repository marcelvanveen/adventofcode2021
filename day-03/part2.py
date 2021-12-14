import sys
import numpy as np

vector = np.array([list(l.strip()) for l in sys.stdin.readlines()]).astype(int)

# oxygen
filtered = vector
for i in range(vector.shape[1]):
    if len(filtered) > 1:
        most_common = 1 if (np.sum(filtered, 0)[i] >= (filtered.shape[0] / 2)) else 0
        filtered = filtered[np.in1d(filtered[:, i], [most_common])]

oxygen = 0
for b in filtered[0]:
    oxygen = (oxygen << 1) | b

# co2
filtered = vector
for i in range(vector.shape[1]):
    if len(filtered) > 1:
        least_common = 0 if (np.sum(filtered, 0)[i] >= (filtered.shape[0] / 2)) else 1
        filtered = filtered[np.in1d(filtered[:, i], [least_common])]

co2 = 0
for b in filtered[0]:
    co2 = (co2 << 1) | b

print(oxygen * co2)