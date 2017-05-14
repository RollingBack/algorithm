#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/14 下午4:39
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : p49.py
# @Software: PyCharm
from itertools import permutations
from itertools import combinations
from euler import is_prime
base = list('123456789')*4
print(base)
def is_arithmetic_sequence(x):
    x.sort()
    return x[2] - x[1] == x[1] - x[0] != 0

for each_combin in combinations(base, 4):
    prime_list = []
    for each in permutations(each_combin):
        each = int(''.join(each))
        if is_prime(each):
            prime_list.append(each)
    if len(prime_list) >= 3:
        for e in combinations(prime_list, 3):
            if is_arithmetic_sequence(list(e)):
                print(e)
