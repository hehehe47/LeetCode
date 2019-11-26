#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/8 17:59 
# @Author : Patrick 
# @File : Twitter New Office Design.py 
# @Software: PyCharm

def calculateHeight(hl, hr, distance):
    if distance == 1:
        return min(hl, hr) + 1
    if hl == hr:
        return hl + (distance // 2 if distance % 2 == 0 else distance // 2 + 1)
    if distance > abs(hl - hr):
        distance -= abs(hl - hr)
        minh = min(hl, hr) + abs(hl - hr)

        return minh + (distance // 2 if distance % 2 == 0 else distance // 2 + 1)

    return min(hl, hr) + distance


def maxHeight(tablePositions, tableHeights):
    if not tableHeights or not tablePositions or len(tableHeights) != len(tablePositions):
        return 0
    ans = 0
    for i in range(1, len(tablePositions)):
        ans = max(ans,
                  calculateHeight(tableHeights[i - 1], tableHeights[i], tablePositions[i] - tablePositions[i - 1] - 1))
    return ans


print(maxHeight([1, 2, 4, 7], [4, 5, 7, 11]))  # 9
print(maxHeight([1, 3, 7], [4, 3, 3]))  # 5
print(maxHeight([1, 10], [1, 5]))  # 7
