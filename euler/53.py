#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 26/05/2017 4:30 PM
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : 53.py
# @Software: PyCharm Community Edition


def factorial(x):
    product = 1
    for x in range(x, 0, -1):
        product *= x
    return product


def C(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))


def gt_million(n, r):
    return C(n, r) > 1000000


print(C(5, 3))
total = 0
for n in range(1, 101):
    for r in range(1, n+1):
        if gt_million(n, r):
            total += 1
print(total)

