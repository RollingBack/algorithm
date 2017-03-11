# -*- coding: utf-8 -*-
from itertools import repeat


def lattice_paths(x):
    lattice = [list(repeat(1, x+1))]
    for i in range(1, x+1):
        l = [1]
        for y in range(1, x+1):
            l.append(lattice[i-1][y]+l[y-1])
        lattice.append(l)
    return lattice[-1][-1]

print(lattice_paths(20))
