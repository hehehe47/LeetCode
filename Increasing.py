#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/16 16:13 
# @Author : Patrick 
# @File : Increasing.py 
# @Software: PyCharm


def almostIncreasingSequence(sequence):
    c = 0
    d = {}
    for i in sequence:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    for v in d.values():
        if v > 2 or c > 1:
            return False
        elif v > 1:
            c += 1
    if c > 1:
        return False
    for i in range(len(sequence) - 1):
        if sequence[i] > sequence[i + 1]:
            tmp = sequence[0:i] + sequence[i + 1:]
            if tmp == sorted(tmp):
                return True
    tmp = sequence[:-1]
    if tmp == sorted(tmp):
        return True
    return False


print(almostIncreasingSequence([1, 1]))
