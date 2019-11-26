#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/23 17:18 
# @Author : Patrick 
# @File : first_largest_increasing.py
# @Software: PyCharm

def isincrease(n):
    n = str(n)
    for j in range(len(n) - 1):
        if n[j] >= n[j + 1]:
            return False
    return True


def output(num):
    for i in range(num, 1, -1):
        if isincrease(i):
            return i
    return 0


n = int(input())
print(output(n))
