#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/11 下午5:29
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : truncatable_primes.py
# @Software: PyCharm
from euler import is_prime
from itertools import count
import re

def is_trunc(x):
        y = str(x)
        for i in range(1, len(y)):
            if not is_prime(int(y[i:])) or not is_prime(int(y[:-i])):
                return False
        return True

total = 0
sum1 = 0
for each in count(11):
    if not (each > 100 and re.search('[245680]', str(each))):
        # print(each)
        if is_prime(each) and is_trunc(each):
            total += 1
            sum1 += each
            if total == 11:
                break
print(sum1)



from euler import is_prime
import re
n, f = 11, 1
tp = []

def is_trunc(n):
    for d in range(1, len(str(n))):
        if not is_prime(str(n)[d:]) or not is_prime(str(n)[:d]):
            return False
    return True

while len(tp) < 11:
    # n += 3-f    # fast count for prime candidates
    # f = -f
    if not (n > 100 and re.search('[245680]', str(n))):
        if is_prime(n) and is_trunc(n):
            tp.append(n)
    n += 1

print ("Project Euler 37 Solution =", sum(tp),  tp)