#!/usr/bin/env python
# -*- coding: utf-8 -*-
from euler import is_prime
from itertools import permutations
full_digit = list('123456789')
l = []
while True:
    full_digit_all = permutations(full_digit)
    for each in full_digit_all:
        if each[-1] not in ['2', '4', '5', '6', '8']:
            num = int(''.join(each))
            if is_prime(num):
                l.append(num)
    if len(full_digit) < 4:
        break
    full_digit.pop()
print(max(l))