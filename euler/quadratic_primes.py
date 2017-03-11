# -*- coding: utf-8 -*-

# n^2+an+b
def is_prime(x):
    for y in range(2, x):
        if x%y == 0:
            return False
    return True

from itertools import count

def get_max_prime_num(a, b):
    for i in count():
        result = pow(i,2)+a*i+b
        if result < 0 or not is_prime(result):
            return i
l = []
for a in range(-999, 1000):
    for b in range(-999, 1000):
        l.append((get_max_prime_num(a, b), a*b))
print(max(l))
