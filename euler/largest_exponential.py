# -*- coding: utf-8 -*-
from decimal import *

getcontext().prec = 28
with open("./p099_base_exp.txt") as f:
    data = f.readlines()


def to_tuple(x):
    return tuple(map(int, x.replace("\n", "").split(",")))


def bigger_data(x, y):
    a, b = x
    c, d = y
    if b < d:
        result = Decimal(a) / Decimal(pow(c, Decimal(d) / Decimal(b)))
    else:
        result = Decimal(pow(a, Decimal(b) / Decimal(d))) / Decimal(c)
    if result > 1:
        return True
    return False


big = list(map(to_tuple, data))
largest_tuple = big[0]
line_no = 1
big_line = 0
for each_tuple in big:
    if bigger_data(each_tuple, largest_tuple):
        largest_tuple = each_tuple
        big_line = line_no
    line_no += 1
print(big_line)

