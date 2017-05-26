#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 26/05/2017 2:28 PM
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : 51.py
# @Software: PyCharm Community Edition
from euler import is_prime


class MyDict(dict):
    def __missing__(self, key):
        self[key] = is_prime(key)
        return self[key]


class Prime(object):
    def __init__(self):
        self.data = MyDict()
        for each_prime in [x for x in range(2, 1000) if is_prime(x)]:
            self.data[each_prime] = True

    def __iter__(self):
        if len(self.data) > 0:
            return self.data.__iter__()
        return {}.__iter__()

    def __getitem__(self, item):
        return self.data[item]

pl = Prime()
def eight_prime_family(prime, rd):
    prime = str(prime)
    count = 0
    for digit in '0123456789':
        n = prime.replace(rd, digit)
        if n.startswith('0'):
            continue
        n = int(n)
        if pl[n]:
            count += 1
    return count == 8

for i in range(11, 1000000, 2):
    if pl[i] and i%10 in (1, 3, 7, 9):
        if str(i).count('0') >= 3 or str(i).count('1') >= 3 or str(i).count('2') >=3:
            if eight_prime_family(i, '0') or eight_prime_family(i, '1') or eight_prime_family(i, '2'):
                print(i)
                break

