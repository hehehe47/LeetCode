#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/30 23:14 
# @Author : Patrick 
# @File : 2.py 
# @Software: PyCharm


def dis(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


line = '4 4 4 3'
n, xc, yc, r = list(map(int, line.split()))
l = []
ans = []
for i in range(0, n):
    for j in range(0, n):
        l.append(dis(j, i, xc, yc))
        l.append(dis(j, i + 1, xc, yc))
        l.append(dis(j + 1, i, xc, yc))
        l.append(dis(1 + j, i + 1, xc, yc))
        ma, mi = max(l), min(l)
        if ma > r > mi:
            ans.append(i * n + j + 1)
        l = []
if ans:
    print(' '.join(list(map(str, ans))))
else:
    print(-1)
