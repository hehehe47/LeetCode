#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/2 20:34 
# @Author : Patrick 
# @File : Genre.py
# @Software: PyCharm

import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        print(line[:-1] + (chr(ord(line[-1]) + ord('A') - ord('a')) if line[-1].islower() else line[-1]))
