# -*- coding: utf-8 -*-


def fib(x):
    a, b = 0, 1
    for i in range(x):
        a, b = b, a+b
    return b


for i in range(1, 10000000):
    if len(str(fib(i))) >= 1000:
        print(i)
        break