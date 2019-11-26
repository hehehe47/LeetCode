#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/29 15:45 
# @Author : Patrick 
# @File : classroom.py
# @Software: PyCharm

s = '[[[tshirt,a]],[[[b]],doll],toy,apple]'
# s = '[[tshirt,a],[b,doll],toy,apple]'
# s = '[[[apple]]]'
count = 0
depth = -float('inf')
for i in s:
    if i == '[':
        count += 1
    elif i == ']':
        count -= 1
    if count > depth:
        depth = count
string = ''

count = 0
d = {i: [] for i in range(1, depth + 1)}
for i in s:
    if i == '[':
        count += 1
    elif i == ']':
        if string:
            d[count].append(string)
        string = ''
        count -= 1
    elif string == '' and i == ',':
        continue
    else:
        string += i
string2 = ''
for i in range(depth, 0, -1):
    string2 = ''
    for idx, j in enumerate(d[i]):
        string2 += '[' + j + ']' + (',' if len(d[i]) > 1 and idx != len(d[i]) - 1 else '')
    print(string2)
