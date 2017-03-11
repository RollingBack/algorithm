# -*- coding: utf-8 -*-
from itertools import groupby
def get_factors(x):
    l = []
    for i in range(1, x):
        if x % i == 0:
            l.append(i)
    return sum(l)

def flip_tuple(t):
    x, y = t
    return y, x

def not_mirror_tuple(t):
    x, y = t
    return x != y



tp = [(x, get_factors(x)) for x in range(1, 10000)]
print(sum([x for x, y in filter(lambda x: flip_tuple(x) in tp and not_mirror_tuple(x), tp)]))
