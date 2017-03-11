# -*- coding: utf-8 -*-

from max_prime_factor import is_prime
import threading
from queue import Queue

q = Queue()
result = []


def sum_prime(x, y):
    total = 0
    for x in range(x, y):
        if is_prime(x):
            total += x
    q.put(total)

if __name__ == "__main__":
    t1 = threading.Thread(target=sum_prime, args=(2, 1000001))
    t2 = threading.Thread(target=sum_prime, args=(1000001, 2000001))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    while not q.empty():
        result.append(q.get())
    print(sum(result))
