# -*- coding: utf-8 -*-
from itertools import count
from euler import fib

for i in count():
    if len(str(fib(i))) >= 1000:
        print(i+1)
        break