#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/9 16:14 
# @Author : Patrick 
# @File : countpattern.py 
# @Software: PyCharm

def doSomething(blob, pattern):
    blob = '|'.join(blob).strip()
    if not pattern:
        return '0|' * (blob.count('|') + 1) + '0'
    l = []
    count = 0
    for i in range(len(blob) - 1):
        if blob[i] == '|':
            l.append(count)
            count = 0
            continue
        if blob[i:i + len(pattern)] == pattern:
            count += 1
    l.append(count)
    l.append(sum(l))
    return '|'.join([str(j) for j in l])


print(doSomething('bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32', 'bc'))
print(doSomething('aaaakjlhaa|aaadsaaa|easaaad|sa', 'aa'))
print(doSomething('bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32', 'b'))
print(doSomething('bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32', ''))
