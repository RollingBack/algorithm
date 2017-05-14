#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/11 下午3:42
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : euler.py
# @Software: PyCharm
from math import sqrt
def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
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

def trial_division(x):
    if x < 2:
        return []
    prime_factors = []
    for y in prime_sieve(int(sqrt(x))):
        while True:
            remain, mod = divmod(x, y)
            if mod == 0:
                prime_factors.append(y)
                x = remain
            else:
                break
    if x != 1:
        prime_factors.append(x)
    return prime_factors


def prime_sieve(x):
    for i in range(2, x+1):
        if is_prime(i):
            yield i

def gcd(x, y):
    while y != 0:
        y, x = x % y, y
    return x
        
class PrimeList(dict):
    def __init__(self, x):
        super().__init__(self)
        for i in range(x+1):
            if is_prime(i):
                self[i] = True
            else:
                self[i] = False

    def __missing__(self, key):
        if is_prime(key):
            self[key] = True
        else:
            self[key] = False
        return self[key]
