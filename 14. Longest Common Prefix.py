#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/12 23:05 
# @Author : Patrick 
# @File : 14. Longest Common Prefix.py 
# @Software: PyCharm


def longest(str):
    str.reverse()
    print(str)
    # if len(str) == 0:
    #     return ""
    # prefix = str[0]
    # for i in range(1, len(str)):
    #     while str[i].index(prefix) != 0:
    #         prefix = prefix[0:len(prefix) - 1]
    # # return prefix
    str = reversed(str)
    for i in str:
        print(i)
    print(str)


print(longest(['leets', 'leetcode', 'leet', 'leeds']))
