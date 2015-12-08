#!/usr/bin/python
import numpy as np

puzzleinput = None
with open('input.txt', 'r') as f:
    puzzleinput = f.readlines()

code = 0
mem = 0

for line in puzzleinput:
    line = line.strip()
    mem += len(line)
    encoded = line.replace('\\', '\\\\')
    encoded = encoded.replace('\"', '\\\"')
    encoded = encoded.replace('\'', '\\\'')
    encoded = '\"' + encoded + '\"'
    code += len(encoded)
    print line, len(line)
    print encoded, len(encoded)

print code - mem
