# -*- coding: utf-8 -*-



def is_multiple(x):
    for y in range(1, 21):
        if x%y != 0:
            return False
    return True


for x in range(1, 100000000000):
    if is_multiple(x):
        print(x)
        break
