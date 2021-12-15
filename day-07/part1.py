import sys
import numpy as np

crab_locations = list(map(int, sys.stdin.readline().strip().split(",")))

min_location = min(crab_locations)
max_location = max(crab_locations)
location_range = max_location - min_location

fuel_costs = [0] * (location_range+1)
for loc in crab_locations:
    for r in range(min_location, max_location+1):
        fuel_costs[r] += abs(r - loc)

print(min(fuel_costs))