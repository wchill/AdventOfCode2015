#!/usr/bin/python
import re
puzzleinput = None
with open('input.txt', 'r') as f:
    puzzleinput = f.readlines()

total = 0
vowels = 'aeiou'
letters = 'abcdefghijklmnopqrstuvwxyz'

def first(line):
    pos = re.search(r'(..).*\1', line)
    return pos is not None

def second(line):
    pos = re.search(r'(.).\1', line)
    return pos is not None

for line in puzzleinput:
    line = line.strip()
    if first(line) and second(line):
        total += 1
print total
