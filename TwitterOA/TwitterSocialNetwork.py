#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/26 17:19 
# @Author : Patrick 
# @File : TwitterSocialNetwork.py 
# @Software: PyCharm


def countGroups(related):
    if not related:
        return 0
    grid = [list(i) for i in related]
    count = 0
    length = len(grid[0])
    visited = [False for _ in range(len(grid))]

    def dfs(i):
        # if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or visited[i * length + j] == 1 or grid[i][j] != '1':
        if i > length or visited[i]:
            return 0
        visited[i] = True
        for k in range(len(grid[i])):
            if grid[i][k] == '1':
                dfs(k)
        # dfs(i + 1, j)
        # dfs(i - 1, j)
        # dfs(i, j - 1)

    for i in range(len(grid)):
        if not visited[i]:
            dfs(i)
            count += 1

    return count


print(countGroups(['1100', '1110', '0110', '0001']))
print(countGroups(['10000', '01000', '00100', '00010', '00001']))
# print(countGroups(['10100', '01000', '10100', '00010', '00001']))
