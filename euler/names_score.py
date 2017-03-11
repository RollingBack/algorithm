# -*- coding: utf-8 -*-

with open("./p022_names.txt", "r") as f:
    names = f.readline().replace('"', "")


def ord_chr(x):
    return ord(x)-64


def cal_name_score(x, rank):
    l = list(x)
    return rank*(sum(map(ord_chr, l)))

names_list = sorted(names.split(","))

start = 1
total = 0
for each_name in names_list:
    if each_name == "COLIN":
        print(start)
    total += cal_name_score(each_name, start)
    start += 1
print(total)