# -*- coding: utf-8 -*-

from functools import reduce

def square_sum():
    return sum([a*a for a in range(1,101)])

def sum_square():
    return pow(reduce(lambda x, y: x+y, [a for a in range(1, 101)]), 2)


print(sum_square()-square_sum())