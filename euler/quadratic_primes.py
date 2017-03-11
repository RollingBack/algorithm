# -*- coding: utf-8 -*-

from itertools import count
from euler import is_prime


def get_max_prime_num(a, b):
    for i in count():
        result = pow(i,2)+a*i+b
        if result < 0 or not is_prime(result):
            return i
l = []
for a in range(-999, 1000):
    for b in range(-999, 1000):
        l.append((get_max_prime_num(a, b), a*b))
print(max(l))
