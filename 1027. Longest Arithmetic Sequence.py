#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/12 18:05 
# @Author : Patrick 
# @File : 1027. Longest Arithmetic Sequence.py 
# @Software: PyCharm


def longestArithSeqLength(A):
    d = {}
    l = []
    diff = [[-1 for _ in range(len(A))] for _ in range(len(A))]
    visited = [[False for _ in range(len(A))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(i, len(A)):
            diff[i][j] = A[i] - A[j]

    for a in range(len(A)):
        for b in range(a, len(A)):
            if not visited[a][b] and diff[a][b] != -1:
                tmp = set()
                tmp.add(A[a])
                tmp.add(A[b])
                helper(A, diff, visited, a, b, tmp)
                l.append(tmp)
    print(l)
    return max([len(z) for z in l])


def helper(A, diff, visited, a, b, l):
    if diff[a][b] == -1 or visited[a][b]:
        return

    for k in range(b + 1, len(diff)):
        if diff[b][k] == diff[a][b]:
            # l.append(A[b])
            visited[a][b] = True
            l.add(A[k])
            helper(A, diff, visited, b, k, l)


# print(longestArithSeqLength(
#     [12, 28, 13, 6, 34, 36, 53, 24, 29, 2, 23, 0, 22, 25, 53, 34, 23, 50, 35, 43, 53, 11, 48, 56, 44, 53, 31, 6, 31, 57,
#      46, 6, 17, 42, 48, 28, 5, 24, 0, 14, 43, 12, 21, 6, 30, 37, 16, 56, 19, 45, 51, 10, 22, 38, 39, 23, 8, 29, 60,
#      18]))

print(longestArithSeqLength(
    [22, 8, 57, 41, 36, 46, 42, 28, 42, 14, 9, 43, 27, 51, 0, 0, 38, 50, 31, 60, 29, 31, 20, 23, 37, 53, 27, 1, 47, 42,
     28, 31, 10, 35, 39, 12, 15, 6, 35, 31, 45, 21, 30, 19, 5, 5, 4, 18, 38, 51, 10, 7, 20, 38, 28, 53, 15, 55, 60, 56,
     43, 48, 34, 53, 54, 55, 14, 9, 56, 52]))  # 6
