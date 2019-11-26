#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Patrick
# @Software: PyCharm


def check_anagram(m, n):
    if len(m) != len(n):
        return -1
    count = 0
    # for idx,i in enumerate(m):
    #     if i!=n[len(n)-idx-1]:
    #         count+=1
    # return count
    l = [0] * 26
    for i in m:
        l[ord(i) - ord('a')] += 1
    for j in n:
        l[ord(j) - ord('a')] -= 1
    return sum([abs(k) for k in l]) / 2


def getMinimumDifference(a, b):
    # Write your code here
    if len(a) != len(b):
        return []
    ans = []
    for i in range(len(a)):
        ans.append(check_anagram(a[i], b[i]))
    return ans


print(getMinimumDifference(['a', 'jk', 'abb', 'mn', 'abc'], ['bb', 'kj', 'bbc', 'op', 'def']))
