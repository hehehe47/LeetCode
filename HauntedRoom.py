#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/16 16:37 
# @Author : Patrick 
# @File : HauntedRoom.py 
# @Software: PyCharm


def matrixElementsSum(matrix):
    can = [k for k in range(len(matrix[0]))]
    c = 0
    for i in range(len(matrix)):
        if not can:
            return c
        tmp = can.copy()
        for j in can:
            if matrix[i][j] != 0:
                c += matrix[i][j]
            else:
                tmp.pop(tmp.index(j))
        can = tmp.copy()
    return c


print(matrixElementsSum([[1, 1, 1, 0],
                         [0, 5, 0, 1],
                         [2, 1, 3, 10]]))
print(matrixElementsSum([[1, 1, 1],
                         [2, 2, 2],
                         [3, 3, 3]]))
