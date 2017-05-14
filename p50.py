#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/14 下午5:05
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : p50.py
# @Software: PyCharm

from euler.euler import is_prime, PrimeList
from itertools import count

pl = PrimeList(10000)
def prime(s):
    total = 0
    for y in count(s, 1):
        if pl[y]:
            total += y
            if total < 1000000:
                yield y
            else:
                raise StopIteration

for each in prime(2):
    total = 0
    for each_prime in prime(each):
        total += each_prime
    if is_prime(total):
        print(total)
        break

