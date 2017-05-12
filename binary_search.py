#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/12 下午10:00
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : binary_search.py
# @Software: PyCharm

def binary_search(x, needle):
    low = 0
    high = len(x) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = x[mid]
        if guess == needle:
            return mid
        if guess > needle:
            high = mid - 1
        else:
            low = mid + 1
    return None

def linear_search(x, needle):
    length = len(x)
    for index in range(length):
        if x[index] == needle:
            return index
    return None

if __name__ == '__main__':
    print(binary_search([x for x in range(10)], 7))
