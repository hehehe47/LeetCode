#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/2 20:46 
# @Author : Patrick 
# @File : 2.py 
# @Software: PyCharm


import sys

if __name__ == "__main__":
    # 读取第一行的n

    n, m = list(map(int, sys.stdin.readline().strip().split()))
    bit = list(sys.stdin.readline().strip())
    count = [0] * len(bit)
    d = {}
    for i in range(m):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        x, y = list(map(int, line.split()))
        if x > y:
            tmp = y
            y = x
            x = tmp
        for i in range(x - 1, y):
            if d.get(i, None):
                d[i] += 1
            else:
                d[i] = 1
    for j in range(len(bit)):
        if d[j] and d[j] % 2 == 1:
            if bit[j] == '1':
                bit[j] = '0'
            else:
                bit[j] = '1'

    print(''.join(bit))
