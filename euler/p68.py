#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import combinations, permutations

def good(x):
    if sum([x[0], x[6], x[7]]) != sum([x[1], x[7], x[8]]):
        return False
    if sum([x[0], x[6], x[7]]) !=  sum([x[2], x[8], x[9]]):
        return False
    if sum([x[0], x[6], x[7]]) != sum([x[3], x[9], x[5]]):
        return False
    if sum([x[0], x[6], x[7]]) != sum([x[4], x[5], x[6]]):
        return False
    return True

r = []
for each in filter(good, permutations(range(1, 11))):
    line_1 = [each[4], each[5], each[6]]
    line_2 = [each[0], each[6], each[7]]
    line_3 = [each[1], each[7], each[8]]
    line_4 = [each[2], each[8], each[9]]
    line_5 = [each[3], each[9], each[5]]
    minguy = min([each[4], each[0], each[1], each[2], each[3]])
    if each[4] == minguy:
        big = line_1 + line_2 + line_3 + line_4 + line_5
    elif each[0] ==  minguy:
        big = line_2 + line_3 + line_4 + line_5 + line_1
    elif each[1] == minguy:
        big = line_3 + line_4 + line_5 + line_1 + line_2
    elif each[2] == minguy:
        big = line_4 + line_5 + line_1 + line_2 + line_3
    elif each[3] == minguy:
        big = line_5 + line_1 + line_2 + line_3 + line_4
    r.append(''.join(map(str, big)))    
print(max(map(int, filter(lambda x: len(x) == 16, r))))
