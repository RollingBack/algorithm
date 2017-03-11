#-*- coding: utf-8 -*-

def is_prime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

count = 0
for x in range(2, 10000000):
    if is_prime(x):
        count += 1
    if count == 10_001:
        print(x)
        break

