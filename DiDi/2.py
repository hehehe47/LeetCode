#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/12/4 21:25 
# @Author : Patrick 
# @File : 2.py 
# @Software: PyCharm


def solution(n):
    if n < 0:
        neg = -1
    else:
        neg = 1
    succ = False
    num = str(abs(n))
    for idx, i in enumerate(num):
        if (int(i) < 5 and neg == 1) or (int(i) > 5 and neg == -1):
            num = num[:idx] + '5' + num[idx:]
            succ = True
            break
    if not succ:
        num += '5'

    num = int(num)
    return num * neg


print(solution(268))
print(solution(670))
print(solution(567))
print(solution(0))
print(solution(-999))
