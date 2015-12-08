#!/usr/bin/python
import numpy as np

puzzleinput = None
with open('input.txt', 'r') as f:
    puzzleinput = f.readlines()

lights = np.zeros((1000,1000))

for line in puzzleinput:
    line = line.strip()
    parts = line.split(' ')
    if line.startswith('turn on'):
        x1, _, y1 = parts[2].partition(',')
        x2, _, y2 = parts[4].partition(',')
        lights[int(x1):int(x2)+1, int(y1):int(y2)+1] = 1
    elif line.startswith('turn off'):
        x1, _, y1 = parts[2].partition(',')
        x2, _, y2 = parts[4].partition(',')
        lights[int(x1):int(x2)+1, int(y1):int(y2)+1] = 0
        lights[lights < 0] = 0
    else:
        x1, _, y1 = parts[1].partition(',')
        x2, _, y2 = parts[3].partition(',')
        lights[int(x1):int(x2)+1, int(y1):int(y2)+1] = 1 - lights[int(x1):int(x2)+1, int(y1):int(y2)+1]
print np.sum(lights)
