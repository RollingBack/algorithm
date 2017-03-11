#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/11 上午9:22
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : pandigital_products.py
# @Software: PyCharm Community Edition
from itertools import count, takewhile

total = 0
S = set()
for x in takewhile(lambda x: x<10000, count(1)):
    for y in count(1):
        product = x * y
        all = str(x)+ str(y) + str(product)
        l = len(all)
        if l == 9 and all.find("0") == -1:
            if len(set(all)) == 9:
                S.add(product)
        elif l > 9:
            break
print(sum(S))