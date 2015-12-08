#!/usr/bin/python
import numpy as np

puzzleinput = None
with open('input.txt', 'r') as f:
    puzzleinput = f.readlines()

wires = {}

def read():
    for line in puzzleinput:
        line = line.strip()
        inputs, _, output = line.partition(' -> ')
        wires[output] = inputs.split(' ')

def solve(wire):
    if wire not in wires:
        return int(wire)
    if isinstance(wires[wire], (int, long)):
        return wires[wire]
    res = None
    op = wires[wire]
    if op[0] == 'NOT':
        res = (~solve(op[1]) & 0xFFFF)
    elif len(op) == 1:
        res = solve(op[0])
    elif op[1] == 'OR':
        res = solve(op[0]) | solve(op[2])
    elif op[1] == 'AND':
        res = solve(op[0]) & solve(op[2])
    elif op[1] == 'LSHIFT':
        res = (solve(op[0]) << int(op[2])) & 0xFFFF
    else:
        res = (solve(op[0]) >> int(op[2])) & 0xFFFF
    wires[wire] = res
    return res

read()
print solve('a')
