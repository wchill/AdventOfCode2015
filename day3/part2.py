#!/usr/bin/python
puzzleinput = None
with open('input.txt', 'r') as f:
    puzzleinput = f.read()

visited = {}
x1 = 0
y1 = 0
x2 = 0
y2 = 0
for idx, ch in enumerate(puzzleinput):
    if idx % 2 == 0:
        x = x1
        y = y1
    else:
        x = x2
        y = y2
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
    if idx % 2 == 0:
        x1 = x
        y1 = y
    else:
        x2 = x
        y2 = y
print len(visited)
