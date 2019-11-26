#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/19 22:53 
# @Author : Patrick 
# @File : winner.py 
# @Software: PyCharm


def winner(andrea, maria, s):
    # Write your code here
    score_and, score_mar = 0, 0
    i = 0 if s == 'Even' else 1
    a = andrea[i:]
    m = maria[i:]
    j = 0
    while j < len(a):
        if j % 2 == 0:
            score_and += a[j] - m[j]
            score_mar += m[j] - a[j]
        j += 1
    if score_and == score_mar:
        return 'Tie'
    elif score_and > score_mar:
        return 'Andrea'
    else:
        return 'Maria'


print(winner([1, 2, 3], [2, 1, 3], 'Odd'))
