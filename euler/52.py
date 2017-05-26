#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 26/05/2017 4:14 PM
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : 52.py
# @Software: PyCharm Community Edition

def get_same_digits(x, y):
    x = set(str(x))
    y = set(str(y))
    return x == y

for i in range(100, 1000000):
    if not get_same_digits(i, 2*i):
        pass
    else:
        if not get_same_digits(i, 3*i):
            pass
        else:
            if not get_same_digits(i, 4*i):
                pass
            else:
                if not get_same_digits(i, 5*i):
                    pass
                else:
                    if not get_same_digits(i, 6*i):
                        pass
                    else:
                        print(i)
                        break