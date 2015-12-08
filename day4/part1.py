#!/usr/bin/python
import hashlib

puzzleinput = 'yzbqklnj'

h = 'F' * 32
i = 0

while not h.startswith('00000'):
    i += 1
    m = hashlib.md5()
    m.update(puzzleinput)
    m.update(str(i))
    h = m.hexdigest()
print i
