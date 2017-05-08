#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/13 上午11:11
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : multi_process.py
# @Software: PyCharm
from multiprocessing import Queue, Process, Pool, cpu_count
from time import sleep


def producer(q):
    for i in range(1, 100001):
        q.put(i)
    q.put(-1)


def customer(q, r):
    total = 0
    while True:
        item = q.get()
        if item == -1:
            r.put(total)
            return
        total += item


if __name__ == "__main__":
    cpu_num = cpu_count()
    q = Queue()
    r = Queue()
    p1 = Process(target=producer, args=(q, ))
    p2 = Process(target=customer, args=(q, r))
    p1.start()
    p2.start()
    print(r.get())
    p1.join()
    p2.join()
