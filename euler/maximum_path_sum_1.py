# -*- coding: utf-8 -*-

# original_data = """75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
# original_data = """3
# 7 4
# 2 4 6
# 8 5 9 3"""
with open("./p067_triangle.txt", 'r') as f:
    original_data = f.readlines()


def split_to_ints(string):
    return tuple(map(int, string.split(" ")))


# original_data = original_data.splitlines()
original_data = list(map(split_to_ints, original_data))
print(original_data)
# total_lines = len(original_data)
# for i in range(total_lines-1, -1, -1):
#     for m in range(0, len(original_data[i])-1):
#         original_data[i-1][m] += max(original_data[i][m], original_data[i][m+1])
# print(original_data[0][0])


def max_transform(x):
    x = list(x)
    l = len(x)
    for i in range(0, l-1):
        x[i] = max(x[i], x[i+1])
    return tuple(x)


def tuple_sum(x, y):
    return list(map(sum, zip(x, y)))


def reduce_list(data):
    if len(data) == 1:
        return data[0]
    data[-2] = tuple(tuple_sum(max_transform(data[-1]), data[-2]))
    data = data[:-1]
    return reduce_list(data)
print(original_data)
print(reduce_list(original_data))
