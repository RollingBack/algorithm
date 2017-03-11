# -*- coding: utf-8 -*-

def factorial(x):
    if x == 0:
        return 1
    return factorial(x-1)*x


print(sum(map(int, list(str(factorial(100))))))