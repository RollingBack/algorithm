# -*- coding: utf-8 -*-


def sum_diagonals(x):
    if x == 1:
        return 1
    return 4*pow(x, 2) - 6*x + 6 + sum_diagonals(x-2)

print(sum_diagonals(1001))