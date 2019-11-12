#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/16 23:44 
# @Author : Patrick 
# @File : permutation.py 
# @Software: PyCharm

def toString(List):
    return ''.join(List)


def permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]

            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack


string = "12345"
n = len(string)
a = list(string)
permute(a, 0, n - 1)
