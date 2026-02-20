# circle_pattern.py

import math

radius = 10

for y in range(-radius, radius + 1):
    for x in range(-radius, radius + 1):
        if math.sqrt(x**2 + y**2) <= radius:
            print("*", end="")
        else:
            print(" ", end="")
    print()