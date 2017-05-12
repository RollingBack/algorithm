#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import count, combinations
from euler import is_prime 

def prime():
    for x in range(3, 1000):
        if is_prime(x):
            yield x
            
def is_prime_pair(pair):
    x, y = pair
    x = str(x)
    y = str(y)
    if is_prime(int(x+y)) and is_prime(int(y+x)):
        return True
    return False

def is_prime_set(s):
    for each_combin in combinations(s, 2):
        if not is_prime_pair(each_combin):
            return False
    return True

ps = []
for each_combin in combinations(prime(), 5):
    if is_prime_set(each_combin):
        ps.append(sum(each_combin))
print(min(ps))
    