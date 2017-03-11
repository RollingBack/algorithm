# -*- coding: utf-8 -*-

# days_in_month = {
#     1: 31,
#     2: 28,
#     3: 31,
#     4: 30,
#     5: 31,
#     6: 30,
#     7: 31,
#     8: 31,
#     9: 30,
#     10: 31,
#     11: 30,
#     12: 31
# }
#
# def is_leap_year(year):
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#
# def get_days_in_month(year):
#     if is_leap_year(year):
#         days_in_month[2] = 29
#     return days_in_month
#
# total_days_in_1900 = sum([v for (k,v) in get_days_in_month(1900).items()])
# print(total_days_in_1900%7)

# total_days = 0
# for year in range(1900, 2001):
#     for each_month in get_days_in_month(year):

import datetime

l = []
for year in range(1901, 2001):
    for each_month in range(1, 13):
        print(year, each_month)
        l.append(datetime.date(year, each_month, 1).strftime("%w"))
print(l)
print(l.count('0'))



