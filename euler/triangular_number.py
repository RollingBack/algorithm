# -*- coding: utf-8 -*-


def count_divisor(x):
    total = 0
    for y in range(1, x+1):
        if x % y == 0:
            total += 1
    return total

triangular_number = 0
for i in range(1, 100000):
    triangular_number += i
    if count_divisor(triangular_number) > 500:
        print(triangular_number)
        break

