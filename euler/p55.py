#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 31/05/2017 3:34 PM
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : p55.py
# @Software: PyCharm Community Edition


def reverse_int(i):
    l = list(str(i))
    l.reverse()
    return int(''.join(l))


def is_lychrel_numbers(x):
    y = 0
    while y < 50:
        x = x + reverse_int(x)
        y = y + 1
        if is_palindromic(x):
            return False
    return True


def is_palindromic(x):
    l = list(str(x))
    mid = len(l) // 2
    for i in range(mid):
        if l[i] != l[len(l)-1-i]:
            return False
    return True


m = 0
for i in range(1, 10000):
    if is_lychrel_numbers(i):
        m += 1
print(m)
