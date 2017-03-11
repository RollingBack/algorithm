# -*- coding: utf-8 -*-


def collatz(x):
    if x%2 == 0:
        return x/2
    else:
        return 3*x+1


def get_collatz_seq_len(x):
    length = 1
    while x != 1:
        x = collatz(x)
        length += 1
    return length

init = 1000000
big_seq_len = 0
big_seq_num = init
while init > 0:
    seq_len = get_collatz_seq_len(init)
    if seq_len > big_seq_len:
        big_seq_len = seq_len
        big_seq_num = init
    init -= 1
print(big_seq_num)

