# -*- coding: utf-8 -*-

from math import ceil

def is_prime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

def get_max_prime_factors(x):
    for i in range(2, int(ceil(x/2))):
        y = x/i
        m = x%i
        if m == 0:
            if is_prime(int(y)):
                return y
    return False

# print(get_max_prime_factors(600851475143))
