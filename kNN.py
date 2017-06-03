#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 02/06/2017 11:19 AM
# @Author  : tianpeng.qi
# @Email    : lackgod@hotmail.com
# @File    : kNN.py
# @Software: PyCharm Community Edition
from struct import Struct
from numpy import *
from multiprocessing import Pool
import timeit
from numexpr import evaluate


# 获取数据
def get_data(path):
    with open(path, 'rb') as file:
        # 获取文件头
        file_content = file.read(16)
        head = Struct('>iiii')
        # 解析文件头
        magic_number, number_of_images, number_of_rows, number_of_columns = head.unpack_from(file_content)
        assert magic_number == 2051, "魔法数字应该为2051"
        # 把图像解析为28*28的向量
        raw = file.read(number_of_columns*number_of_rows)
        final = []
        while raw:
            unsign = Struct('>'+'B'*(number_of_columns*number_of_rows))
            pixel = unsign.unpack_from(raw)
            final.append(list(pixel))
            raw = file.read(number_of_columns*number_of_rows)
        final = array(final)
        # 二值化, 使用numexpr 加速
        return evaluate('where(final > 0, 1, 0)')


# 获取标签
def get_labels(path):
    with open(path, 'rb') as file:
        file_content = file.read(8)
        head = Struct('>ii')
        # 解析头
        magic_number, number_of_labels = head.unpack_from(file_content)
        assert magic_number == 2049, "魔法数字应该为2049"
        raw = file.read(1)
        labels = []
        while raw:
            unsign = Struct('>B')
            labels.append(unsign.unpack_from(raw)[0])
            raw = file.read(1)
        assert number_of_labels == len(labels), '标签数量应该和文件头里记录的数量一致'
        return labels


# 分类器
def classify(mat):
    # 构造同训练数据具有相同shape的矩阵并求差值
    diff_mat = tile(mat[1], (training_data.shape[0], 1)) - training_data
    # 求差值平方
    square_diff = diff_mat ** 2
    # 求和
    square_distance = sum(square_diff, axis=1)
    # 开平方
    distance = square_distance ** 0.5
    # 获取排序后的索引，用来对应标签
    sorted_distance_index = argsort(distance)
    class_count = {}
    for i in range(K):
        label = training_labels[sorted_distance_index[i]]
        try:
            class_count[label] += 1
        except KeyError:
            class_count[label] = 1
    return sorted(class_count.items(), key=lambda x: x[1], reverse=True)[0][0] == test_labels[mat[0]]


# 获取训练图像数据
training_data = get_data('./train-images-idx3-ubyte')
# 获取测试图像数据
test_data = get_data('./t10k-images-idx3-ubyte')
# 为测试数据加上索引，用来测试最终结果的正确度
test_data = enumerate(test_data[:100])
# 获取训练数据的标签
training_labels = get_labels('./train-labels-idx1-ubyte')
# 获取测试数据的标签
test_labels = get_labels('./t10k-labels-idx1-ubyte')
# k值
K = 10


def test():
    # 构造进程池，用来加速处理，默认使用全部cpu核心
    with Pool() as p:
        bool_list = p.map(classify, test_data)
        # 输出测试结果
        print(bool_list.count(False)/float(len(bool_list)))


if __name__ == '__main__':
    # 获取程序执行时间
    t = timeit.Timer('test()', setup='from __main__ import test')
    print(t.timeit(1))
