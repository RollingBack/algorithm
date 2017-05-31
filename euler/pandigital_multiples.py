#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/12 上午9:27
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : pandigital_multiples.py
# @Software: PyCharm
from itertools import count
def concat(args):
    all = ''
    for each in args:
        all += str(each)
    return all

def concatenated_product(x, y):
    return concat(tuple(map(lambda a: x*a, y)))

def is_pandigital(x):
    x = str(x)
    if len(x) != 9:
        return False
    x = set(x)
    if len(x) != 9:
        return False
    return True

c = []
for a in (2, 10):
    for x in count(2):
        b = concat([y*x for y in range(1, a)])
        if len(b) > 9:
            break
        elif len(b) == 9 and b.find('0') == -1:
            if is_pandigital(b):
                print(b)
                c.append(b)
print(max(c))