#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/14 16:55 
# @Author : Patrick 
# @File : Maximal Commonality.py 
# @Software: PyCharm

def maxLCS(s):
    dl, dr = {}, {}
    dcombine = {}
    maxL = 0
    count = 0
    for c in s:
        if dr.get(c, None):
            dr[c] += 1
        else:
            dr[c] = 1
    for i in s:
        if dl.get(i, -1) > 0:
            dl[i] += 1
        else:
            dl[i] = 1
        if dr.get(i, -1) > 0:
            dr[i] -= 1
        else:
            dr[i] = 0
        if dl.get(i, None) and dl.get(i) > 0 and dr.get(i, None) and dr.get(i) > 0:
            if dcombine.get(i):
                dcombine[i] = max(dcombine[i], min(dl[i], dr[i]))
            else:
                dcombine[i] = min(dl[i], dr[i])
    for v in dcombine.values():
        maxL += v
    return maxL


# print(maxLCS('abcdedeara'))  # 3
# print(maxLCS('abcdecdefg'))  # 3
# print(maxLCS('abcdefgh'))  # 0
# print(maxLCS('zzzxxxzzz'))  # 4
# print(maxLCS('aaaa'))  # 2
# print(maxLCS('aaa'))  # 1
# print(maxLCS(''))  # 0
print(maxLCS('abcddddggg'))  # 0
