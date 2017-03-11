# -*- coding: utf-8 -*-

english_number_map = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

def under_hundred_number(x):
    if x < 21:
        return english_number_map[x]
    a, b = divmod(x, 10)
    if b == 0:
        return english_number_map[x]
    return  english_number_map[a*10] + "-" + english_number_map[b]

def number_2_english(x):
    final_string = ""
    a, b = divmod(x, 1000)
    if a >= 1 and a < 21:
        final_string += english_number_map[a]+" thousand "
    elif a >= 21 and a < 100:
        final_string += under_hundred_number(a)+" thousand "
    if b >= 100:
        m, n = divmod(b, 100)
        final_string += english_number_map[m]+" hundred "
        if n > 0:
            final_string += " and "+under_hundred_number(n)
    elif b != 0:
        return under_hundred_number(x)
    return final_string

big_string = ""
for i in range(1, 1001):
    big_string += number_2_english(i)
print(len(big_string.replace(" ", "").replace("-", "")))


