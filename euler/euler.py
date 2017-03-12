#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/11 下午3:42
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : euler.py
# @Software: PyCharm

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(x/2)+1):
        if x%i == 0:
            return False
    return True


def fib(x):
    a, b = 0,1
    for i in range(0, x):
        a, b = b, a+b
    return b


def circular(x):
    l = str(x)
    for i in range(1, len(l)):
        l = l[1:] + l[0]
        yield int("".join(l))


def to_bin(x):
    return '{0:b}'.format(x)


def is_palindromes(x):
    l = list(x)
    l.reverse()
    y = "".join(l)
    return x == y

def return_1(x):
    return 1

def is_circular_primes(x):
    if x == 1:
        return False
    if not is_prime(x):
        return False
    return all(map(is_prime, circular(x)))

class CircularPrime():
    def __init__(self, y):
        self.x, self.y = 1, y

    def __iter__(self):
        return self

    def __next__(self):
        while not is_circular_primes(self.x):
            self.x += 1
        if self.x >= self.y:
            raise StopIteration()
        result = self.x
        self.x += 1
        return result