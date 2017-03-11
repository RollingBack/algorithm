# -*- coding: utf-8 -*-
from itertools import  count, takewhile
from functools import reduce
def factorial(a):
    if a == 0:
        return 1
    return reduce(lambda x, y: x*y, takewhile(lambda x: x <= a, count(1)))

def digit_factorial(a):
    return sum(map(lambda x: factorial(int(x)), list(str(a))))

total = 0
for num in count(1):
    digit_len = len(str(num))
    if pow(10, digit_len-1) > digit_len*factorial(9):
        break
    if num == digit_factorial(num):
        if num != 1 and num != 2:
            total += num
print(total)
