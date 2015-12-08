#!/usr/bin/python
import numpy as np

puzzleinput = None
with open('input.txt', 'r') as f:
    puzzleinput = f.readlines()

code = 0
mem = 0

for line in puzzleinput:
    line = line.strip()
    escaped = line.decode('string-escape')[1:-1]
    code += len(line)
    mem += len(escaped)

print code - mem
