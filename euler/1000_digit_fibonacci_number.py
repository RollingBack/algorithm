# -*- coding: utf-8 -*-
from itertools import count


def fib(x):
    a, b = 0,1
    for i in range(0, x):
        a, b = b, a+b
    return b

for i in count():
    if len(str(fib(i))) >= 1000:
        print(i+1)
        break