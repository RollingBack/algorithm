# -*- coding: utf-8 -*-
from itertools import count
from math import sqrt, floor, ceil
import multiprocessing


def is_complete_square(x):
    root = sqrt(x)
    return x in map(lambda x: x*x, range(floor(root), ceil(root)+1))

def area(x, cir):
    a, b, c = x
    p = cir/2
    m = p*(p-a)*(p-b)*(p-c)
    if is_complete_square(m):
        return sqrt(m)
    return 0


def circumference(x):
    return sum(x)


def worker1():
    total = 0
    for each_triangle in zip(count(2), count(2), count(3)):
        cir = circumference(each_triangle)
        if cir > 1000000000:
            break
        area_of = area(each_triangle, cir)
        if  area_of != 0:
            total += cir
    print(total)
    return total


def worker2():
    total = 0
    for each_triangle in zip(count(2), count(2), count(1)):
        cir = circumference(each_triangle)
        if cir > 1000000000:
            break
        area_of = area(each_triangle, cir)
        if area_of != 0:
            total += cir
    print(total)
    return total

# if __name__ == "__main__":
#     multiprocessing.Process(target=worker1).start()
#     multiprocessing.Process(target=worker2).start()

print(is_complete_square(81))
print(is_complete_square(18))
