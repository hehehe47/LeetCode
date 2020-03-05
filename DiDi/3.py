#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/12/4 21:25 
# @Author : Patrick 
# @File : 3.py 
# @Software: PyCharm

def solution(A):
    ma = -float('inf')
    for i in range(len(A)):
        total_char = set()
        if check(total_char, A[i]):
            ma = max(ma, dfs(i, len(A[i]), len(A[i]), A, total_char)[1])
        if ma == -float('inf') or ma == len(A[i]):
            return 0
    return ma


def check(total_char, string):
    for char in string:
        if char in total_char or string.count(char) > 1:
            return False
    for char in string:
        total_char.add(char)
    return True


def dfs(idx, count, max_l, l, total_char):
    if idx >= len(l) - 1:
        return count, max_l
    for j in range(idx + 1, len(l)):
        if check(total_char, l[j]):
            count += len(l[j])
            count, max_l = dfs(j, count, max_l, l, total_char)
            max_l = max(count, max_l)
            count -= len(l[j])
            for char in l[j]:
                total_char.remove(char)
    return count, max_l


print(solution(['abc', 'cba', 'def', 'gha', 'gi']))
print(solution(
    ['abc', 'def', 'ljaksjdflkjakdf', 'eniansdbfubeaoiafsd', 'jzlkjklnfeibioasdf', 'pekinqoinfenobaibsdufbuabsduf',
     'ebuabsdubfuiabifub', 'g']))

print(solution(['co', 'dil', 'ity']))
print(solution(['abc', 'yyy', 'def', 'csv']))
print(solution(['potato', 'kayak', 'banana', 'racecar']))
print(solution(['eva', 'jqw', 'tyn', 'jan']))
print(solution(['abc']))
