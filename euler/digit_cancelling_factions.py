# -*- coding: utf-8 -*-
from itertools import *
from functools import *

def gcd(x, y):
    if y != 0:
        return gcd(y, x%y)
    return x

def simple(x, y):
    g = gcd(x, y)
    return x/g, y/g

l = []
for first_digital in range(1, 9):
    for second_digital in range(first_digital, 10):
        numerator = int(str(first_digital)+str(second_digital))
        for third_digit in range(1, 10):
            for fourth_digital in range(0, 10):
                denominator = int(str(third_digit)+str(fourth_digital))
                simple1 = simple(numerator, denominator)
                if numerator < denominator:
                    if first_digital == third_digit:
                        s = simple(second_digital, fourth_digital)
                    elif first_digital == fourth_digital:
                        s = simple(second_digital, third_digit)
                    elif second_digital == third_digit:
                        s = simple(first_digital, fourth_digital)
                    elif second_digital == fourth_digital:
                        s = simple(first_digital, third_digit)
                    else:
                        break
                else:
                    continue
                if simple1 == s:
                    l.append((numerator, denominator))
tup = []
for each in zip(*l):
    tup.append(reduce(lambda x, y: x*y, each))
a, b = tuple(tup)
gcd1 = gcd(a, b)
print(b/gcd1)
