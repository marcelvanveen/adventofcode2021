import sys
from lib import count_increments

measurements = [int(l) for l in sys.stdin.readlines()]
print(count_increments(measurements, 1))