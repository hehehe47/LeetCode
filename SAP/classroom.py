#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/11 19:18 
# @Author : Patrick 
# @File : classroom.py
# @Software: PyCharm


def output(classroom):
    ma = -float('inf')
    for i in range(len(classroom)):
        for j in range(len(classroom[0])):
            if classroom[i][j] != '+':
                count = 0
                visit = [[False for _ in range(len(classroom[0]))] for _ in range(len(classroom))]
                count = dfs(i, j, visit, classroom, count)
                ma = max(ma, count)

    return ma


def dfs(i, j, visit, classroom, count):
    if i >= len(classroom) or j >= len(classroom[0]) or i < 0 or j < 0 or classroom[i][j] == '+' or visit[i][j]:
        return count
    visit[i][j] = True
    count += 1
    count = dfs(i, j - 2, visit, classroom, count)
    count = dfs(i, j + 2, visit, classroom, count)
    count = dfs(i - 1, j, visit, classroom, count)
    count = dfs(i + 1, j, visit, classroom, count)

    return count


row = int(input())
coloum = int(input())
if row == 0:
    print(0)
    exit(0)
classroom = []
for i in range(row):
    classroom.append(list(input()))

print(output(classroom))
