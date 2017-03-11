#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/11 下午5:15
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : double_base_palindromes.py
# @Software: PyCharm
from euler import to_bin, is_palindromes

def sum_palindromes_between(x, y):
    total = 0
    for i in range(x, y):
        if is_palindromes(str(i)) and is_palindromes(to_bin(i)):
            total += i
    return total
print(sum_palindromes_between(1, 1000000))



