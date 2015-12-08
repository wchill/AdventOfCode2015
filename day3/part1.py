#!/usr/bin/python
puzzleinput = None
with open('input.txt', 'r') as f:
    puzzleinput = f.read()

visited = {}
x = 0
y = 0
for ch in puzzleinput:
    if ch == '>':
        x += 1
    elif ch == '<':
        x -= 1
    elif ch == '^':
        y += 1
    elif ch == 'v':
        y -= 1
    else:
        continue
    if (x,y) in visited:
        visited[(x,y)] += 1
    else:
        visited[(x,y)] = 1
print len(visited)
