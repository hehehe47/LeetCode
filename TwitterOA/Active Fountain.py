#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/8 21:48 
# @Author : Patrick 
# @File : Active Fountain.py 
# @Software: PyCharm


def fountainActivation(a):
    sort_a = sorted(enumerate(a), reverse=True, key=lambda x: x[1])
    print(sort_a)
    l = [{i: (i - a[i] if i - a[i] >= 0 else 0, i + a[i] if i + a[i] <= len(a) - 1 else len(a) - 1)} for i in
         range(len(a))]

    print(l)


print(fountainActivation([3, 4, 0, 1]))
