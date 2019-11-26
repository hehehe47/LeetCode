#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/23 18:25 
# @Author : Patrick 
# @File : BulidCities.py
# @Software: PyCharm

def fill_city_days(i, j, map, city, days):
    mi = float('inf')
    for ci in city:
        x, y = ci
        mi = min(abs(x - i) + abs(y - j), mi)
    days[i][j] = mi


def output(map):
    count = 0
    visit = [[False for _ in range(len(map[0]))] for _ in range(len(map))]
    days = [[0 for _ in range(len(map[0]))] for _ in range(len(map))]
    city = [(0, 0)]
    ans = 0
    dfs_city(0, 0, map, visit, city, days)
    for i in range(len(map)):
        for j in range(len(map[0])):
            if (i == 0 and j == 0) or map[i][j] == '#' or map[i][j] == '$':
                continue
            else:
                fill_city_days(i, j, map, city, days)
    for k in range(len(map)):
        ans += sum(days[k])
    return ans


def dfs_city(i, j, map, visited, city, days):
    if i >= len(map) or j >= len(map[0]) or i <= 0 or j <= 0 or visited[i][j]:
        return
    visited[i][j] = True
    if map[i][j] == '$':
        fill_city_days(i, j, map, city, days)
        city.append((i, j))

    dfs_city(i - 1, j, map, visited, city, days)
    dfs_city(i, j - 1, map, visited, city, days)
    dfs_city(i + 1, j, map, visited, city, days)
    dfs_city(i, j + 1, map, visited, city, days)


row = int(input())
coloum = int(input())
if row == 0:
    print(0)
    exit(0)
map = []
for i in range(row):
    map.append(list(input()))

print(output(map))
