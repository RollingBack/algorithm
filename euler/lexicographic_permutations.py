# -*- coding: utf-8 -*-

from itertools import permutations


def join_string(x):
    return "".join(x)

sort_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# sort_list = ["0", "1", "2"]
print(sorted(list(map(join_string, permutations(sort_list))))[999999])

# big.sort()
# print(big[1000000])
