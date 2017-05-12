#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import combinations
def P(x):
    return x*(3*x-1)/2

def get_p():
    for i in range(1, 10001):
        yield P(i)
        
p_list = list(get_p())
for each in combinations(p_list, 2):
    x, y = each
    if abs(x-y) in p_list and abs(x+y) in p_list:
        print(x, " ", y, " ", abs(x-y))
        break
