#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/21 21:56 
# @Author : Patrick 
# @File : Cicular Array.py 
# @Software: PyCharm


def circularArray(n, endNode):
    d = {k: 0 for k in range(1, n + 1)}

    start = endNode[0]
    for end in endNode[1:]:
        if end < start:
            end += n
        for j in range(start, end + 1):
            d[j if j <= n else j % n] += 1
        start = end if end <= n else end - n
    m = -float('inf')
    mk = float('inf')
    for key, value in d.items():
        if value > m:
            mk = key
            m = value
    return mk


# Write your code here


print(circularArray(10, [1, 5, 10, 5]))
# print(circularArray(5, [2, 1, 5]))
