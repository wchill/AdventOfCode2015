#!/usr/bin/python
puzzleinput = None
with open('input.txt', 'r') as f:
    puzzleinput = f.readlines()

total = 0
for line in puzzleinput:
    dims = [int(x) for x in line.split('x')]
    dims.sort()
    total += 2 * (dims[0] + dims[1]) + (dims[0] * dims[1] * dims[2])
print total
