#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/14 21:18 
# @Author : Patrick 
# @File : Balanced or not.py 
# @Software: PyCharm

def ba(s):
    l = []
    for i in s:
        if len(l) == 0:
            l.append(i)
            continue
        if i == ')' and l[-1] == '(':
            l.pop()
        else:
            l.append(i)

    return (l)

    a = 1


print(ba('((()()()'))
