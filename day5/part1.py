#!/usr/bin/python
puzzleinput = None
with open('input.txt', 'r') as f:
    puzzleinput = f.readlines()

total = 0
vowels = 'aeiou'
letters = 'abcdefghijklmnopqrstuvwxyz'
for line in puzzleinput:
    if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
        continue
    num_vowels = 0
    for v in vowels:
        num_vowels += line.count(v)
    if num_vowels < 3:
        continue
    for l in letters:
        if l*2 in line:
            total += 1
            break
print total
