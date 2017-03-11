# -*- coding: utf-8 -*-

from functools import reduce

def get_number():
    for a in range(1, 901):
        for b in range(1, 901):
            print("%s * %s" % (1000-a, 1000-b))
            yield (1000-a)*(1000-b)

def is_palindromic_number(number):
    number_list = list(str(number))
    number_list.reverse()
    return "".join(number_list) == str(number)


print(reduce(max, [x for x in get_number() if is_palindromic_number(x)]))