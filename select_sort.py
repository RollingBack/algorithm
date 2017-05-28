#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import shuffle	
from double_link_list import DoubleLinkList
import sys
sys.setrecursionlimit(1000000)

def selectSort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(i+1, length):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr

def insertSort(arr):
    length = len(arr)
    for i in range(1, length):
        key = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] > key:
                arr[j+1] = arr[j]
                arr[j] = key
            j -= 1
        
    return arr

def quickSort(L, low, high):
    if low >= high:
        return L
    i = low 
    j = high    
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j-1                                                             
        L[i] = L[j]
        while i < j and L[i] <= key:    
            i = i+1 
        L[j] = L[i]
    L[i] = key 
    quickSort(L, low, i-1)
    quickSort(L, j+1, high)
    return L
   
def quickSortFunctional(L):
    if len(L) == 0:
        return L
    key = L.pop()
    small = quickSortFunctional([ x for x in L if x <= key])
    big = quickSortFunctional([x for x in L if x > key])
    return small+[key]+big
    
def shellSort(L):
    l = len(L)
    gap = l // 2
    while gap > 0:
        for i in range(gap, l):
            temp = L[i]
            j = i
            while j >= gap and L[j - gap] > temp:
                L[j] = L[j - gap]
                j -= gap
            L[j] = temp
        gap = gap // 2
    return L

def mergeSort(L):
    if len(L) == 1:
        return L
    l = len(L)
    mid = l // 2
    def merge(left, right):
        final = []
        l = len(left)
        r = len(right)       
        a = b = 0
        while a < l and b < r:
            if left[a] > right[b]:
                final.append(right[b])
                b += 1
            else:
                final.append(left[a])
                a += 1
        while a < l:
            final.append(left[a])
            a += 1
        while b < r:
            final.append(right[b])
            b += 1
        return final
    left = mergeSort(L[:mid])
    right = mergeSort(L[mid:])
    return merge(left, right)
    
def kadane(array):
    max_sum = 0
    max_left = 0
    max_right = 0
    current_max = 0
    left = 0
    for i in range(0, len(array)):
        current_max += array[i]
        if current_max > max_sum:
            max_sum = current_max
            right = i
            max_left = left
            max_right = right
        if current_max < 0:
            current_max = 0
            left = i + 1
    return max_left, max_right, max_sum
    
    
    
a = [x for x in range(10)]
shuffle(a)
#print(a[0])
#d = DoubleLinkList(a)
#l = list()
#quickSortFunctional(a)
#a.sort()   
#shellSort(a)
print(mergeSort(a))
