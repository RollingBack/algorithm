#!/usr/bin/env python
# -*- coding: utf-8 -*-
from euler import is_prime
from itertools import count

def odd(x):
    return x%2 != 0


def get_odd_composite_num():
    for i in range(1, 10001):
        if odd(i) and not is_prime(i):
            yield i
            
for each in get_odd_composite_num():
    checker = False
    for i in count(1):
        diff = each - 2*pow(i, 2)
        if diff > 0 and is_prime(diff):
            checker = True
            break
        elif diff <= 0:
            break
    if checker == False:
        print(each)
        break
            
            