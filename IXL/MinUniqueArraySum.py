#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/19 23:14 
# @Author : Patrick 
# @File : MinUniqueArraySum.py 
# @Software: PyCharm


def getMinimumUniqueSum(arr):
    # Write your code here
    a = sorted(arr)
    ans = sum(a)
    l = [i for i in range(min(arr), 3 + min(arr) + (len(arr) if len(arr) > max(arr) else max(arr)))]
    s = set(l)
    for j in arr:
        if j in s:
            l[l.index(j)] = 0
            s.remove(j)
        else:
            for k in range(len(l)):
                if l[k] != 0 and l[k] > j:
                    ans += l[k] - j
                    s.remove(l[k])
                    l[k] = 0
                    break
    return ans


# print(getMinimumUniqueSum([1, 2, 2]))  # 6
# print(getMinimumUniqueSum([1]))  # 1
# print(getMinimumUniqueSum([1, 1, 1, 1, 1]))  # 15
# print(getMinimumUniqueSum([1, 1, 1, 7]))  # 13
# print(getMinimumUniqueSum([2, 2, 2]))  # 9
# print(getMinimumUniqueSum([2, 2, 4, 5]))  # 14
# print(getMinimumUniqueSum([2, 2, 2, 2, 2, 2, 2, 2, 3]))  # 14
# print(sum([2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 14
print(getMinimumUniqueSum([1, 1, 1, 2, 3, 4, 5, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]))  # 317
# print(sum([1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]))  # 317
