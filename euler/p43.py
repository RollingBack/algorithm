#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import permutations
full_digit = '0123456789'

def to_string(x):
    return ''.join(x)

def substring_div(x):
    if x.startswith('0'):
        return False
    div_num = [2, 3, 5, 7, 11, 13, 17]
    for i in range(0, 7):
        if int(x[i+1]+x[i+2]+x[i+3])%div_num[i] != 0:
            return False
    return True
print(sum(map(int, filter(substring_div, map(to_string, permutations(list(full_digit)))))))

