#-*- coding: utf-8 -*-
from euler import is_prime

count = 0
for x in range(2, 10000000):
    if is_prime(x):
        count += 1
    if count == 10_001:
        print(x)
        break

