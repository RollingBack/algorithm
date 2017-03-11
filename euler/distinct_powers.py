# -*- coding: utf-8 -*-
s = set()
for a in range(2, 101):
    for b in range(2, 101):
        s.add(pow(a, b))
print(len(s))
