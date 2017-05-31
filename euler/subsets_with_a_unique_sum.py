#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/12 上午10:23
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : subsets_with_a_unique_sum.py
# @Software: PyCharm
from itertools import combinations, groupby

S = set()
for each in range(1, 100):
    S.add(each*each)
# S = {1, 3, 6, 8, 10, 11}

T = {}
for each in combinations(S, 5):
    sum1 = sum(each)
    if sum1 in T:
        T[sum1] += 1
    else:
        T[sum1] = 1

T = [t for t in T.keys() if T[t] == 1]
print(sum(T))

