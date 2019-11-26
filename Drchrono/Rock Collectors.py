#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/18 17:04 
# @Author : Patrick 
# @File : Rock Collectors.py 
# @Software: PyCharm


def get_rock_index(quantity):
    jamie, ned = quantity, sorted(quantity)
    geoffrey = list(map(lambda x: x[0] + x[1], zip(jamie, ned)))
    fre_idx = {}
    max_count = -float('inf')
    max_par = -float('inf')
    ans_idx = 0
    for idx, partition in enumerate(geoffrey):
        if partition not in fre_idx:
            fre_idx[partition] = (1, idx)
        else:
            fre_idx[partition] = (fre_idx[partition][0] + 1, idx)
        if fre_idx[partition][0] > max_count or (fre_idx[partition][0] == max_count and partition > max_par):
            max_count = fre_idx[partition][0]
            max_par = partition
            ans_idx = fre_idx[partition][1]
    return ans_idx


print(get_rock_index([5, 5, 9, 19, 2, 2]))
print(get_rock_index([10, 10, 7, 7, 7, 2, 7, 2]))
print(get_rock_index([1, 1, 1, 1]))
