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



