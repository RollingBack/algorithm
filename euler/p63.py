#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = set()
for x in range(1, 110):
    for y in range(1, 110):
        r = pow(x, y)
        if len(str(r)) == y:
            print(r)
            s.add(r)
print(len(s))