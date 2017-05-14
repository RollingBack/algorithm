#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/13 下午3:21
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : p47.py
# @Software: PyCharm

from euler import trial_division
from queue import Queue

def distinct_factor_num(x):
    return x, len(set(trial_division(x)))

result = map(distinct_factor_num, range(2*3*5*7, 1000000))
q = []
for x, each in result:
    if each == 4:
        if q != [] and q[-1] != x - 1:
            q = []
        if q == []:
            q.append(x)
            continue
        if  q[-1] == x-1:
            q.append(x)
            print(q)
        if len(q) == 4:
            print(q)
            break


