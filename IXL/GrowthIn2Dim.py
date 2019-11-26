#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/20 0:09 
# @Author : Patrick 
# @File : GrowthIn2Dim.py 
# @Software: PyCharm


def countMax(l):
    y1, x1 = int(l[0].split()[0]), int(l[0].split()[1])
    for i in l[1:]:
        y2, x2 = int(i.split()[0]), int(i.split()[1])
        y1, x1 = min(y1, y2), min(x1, x2)
    return x1 * y1


print(countMax(["2 3", "3 7", "4 1"]))
