#!/usr/bin/python
puzzleinput = None
with open('input.txt', 'r') as f:
    puzzleinput = f.readlines()

total = 0
for line in puzzleinput:
    dims = [int(x) for x in line.split('x')]
    sides = list()
    sides.append(dims[0] * dims[1])
    sides.append(dims[1] * dims[2])
    sides.append(dims[0] * dims[2])
    total += 2 * (sides[0] + sides[1] + sides[2]) + min(sides)
print total
