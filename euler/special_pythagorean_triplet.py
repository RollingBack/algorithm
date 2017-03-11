# -*- coding: utf-8 -*-

def is_pythagorean_triplet(a, b, c):
    return a * a + b * b == c * c

def fit(a, b, c):
    return a + b + c == 1000

def get_number():
    for x in range(1, 1000):
        for y in range(1, 1000):
            for z in range(1, 1000):
                yield x, y, z

print([(a, b, c) for (a, b, c) in get_number() if is_pythagorean_triplet(a, b, c) and fit(a, b, c)])