# -*- coding: utf-8 -*-
from math import ceil


def get_factors(x):
    l = []
    for i in range(1, ceil(x/2)+1):
        if x % i == 0:
            l.append(i)
    return l


def is_abundant_number(x):
    return sum(get_factors(x)) > x

big = set()
abundant_number_list = [x for x in range(1, 28124) if is_abundant_number(x)]
print(abundant_number_list)
for each_number in abundant_number_list:
    for each in abundant_number_list:
        y = each+each_number
        if y < 28124:
            big.add(y)

print(sum([x for x in range(1, 28124) if x not in big]))

