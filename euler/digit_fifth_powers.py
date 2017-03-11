# -*- coding: utf-8 -*-


def fifth_sum(x):
    l = map(int, list(str(x)))
    return sum([pow(x, 5) for x in l])

total = 0
for i in range(2, 5*pow(9,5)):
    if i == fifth_sum(i):
        print(i)
        total += i
print(total)
