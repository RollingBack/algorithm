# -*- coding: utf-8 -*-
# TODO unsolved
with open("./p098_words.txt", 'r') as f:
    words = f.readlines()

words = list(map(lambda x: x.replace('"', ""), words[0].split(",")))
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for each_word in words:
    print(each_word)