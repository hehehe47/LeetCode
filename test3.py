#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/6 15:39 
# @Author : Patrick 
# @File : test3.py 
# @Software: PyCharm
# def findabc(s):
def findabc(s):
    d = {'A': 1, 'B': 1, 'C': 1}
    for k in s:
        if k in d:
            d.pop(k)
        if not d:
            break
    return d


def analyzeInvestments(s):
    # Write your code here
    count = 0
    j = 0
    for i in range(len(s)):
        while j in range(i + 2, len(s)):
            a = findabc(s[i:j + 1])
            if not a:
                j += 1
            else:
                count += len(s) - j
                break
    return count


print(analyzeInvestments('ABBCZBAC'))
print(analyzeInvestments('ABCCBA'))
print(analyzeInvestments('ABC'))
