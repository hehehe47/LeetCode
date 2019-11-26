#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/30 23:41 
# @Author : Patrick 
# @File : 3.py 
# @Software: PyCharm


def transfer(order, num):
    ans = 0
    count = 0
    for i in range(len(num) - 1, -1, -1):
        ans += int(num[i]) * (order ** count)
        count += 1
    return ans


line = '10#11'
d = {}
for i in range(65):
    if i < 10:
        d['i'] = i
    elif i <= 36:
        d[chr(i + ord('a') - 10)] = i
    elif i <= 54:
        d[chr(i + ord('a') - 36)] = i
    elif i == 55:
        d['@'] = i
    else:
        d['_'] = i
d = {chr(j): idx for idx, j in range(ord('a'), ord('z'))}
d = {chr(j): idx + 27 for idx, j in range(ord('a'), ord('z'))}
if (line[:2] == '0x' or line[:2] == '0X') and '#' not in line:
    print(transfer(16, line[2:]))
elif line[:1] == '0' and '#' not in line:
    print(transfer(8, line[1:]))
elif '#' in line:
    l = line.split('#')
    if 2 <= int(l[0]) <= 64 and (l[1] in d or 0 <= int(l[1]) < 10):
        print(transfer(int(l[0]), l[1]))
