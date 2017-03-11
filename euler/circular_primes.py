#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/11 下午3:46
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : circular_primes.py
# @Software: PyCharm
from euler import is_prime, circular, return_1
from multiprocessing import cpu_count, Pool
from euler import is_circular_primes


cpu_num = cpu_count()
if __name__ == "__main__":
    with Pool(cpu_num) as p:
        out = p.map(is_circular_primes, range(1, 1000000))
        out = p.map(int, out)
        # out = p.map(return_1, CircularPrime(1000000))
    print(sum(out))





