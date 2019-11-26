#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/26 17:09 
# @Author : Patrick 
# @File : Autoscale Policy.py 
# @Software: PyCharm
def finalInstances(instances, averageUtil):
    # Write your code here
    i = 0
    while i < len(averageUtil):
        if averageUtil[i] > 60:
            if instances <= 2 * 10 ** 8:
                instances *= 2
                i += 10
        elif averageUtil[i] < 25:
            if instances > 1:
                instances = int(instances / 2 if (instances) % 2 == 0 else ((instances + 1) / 2))
        i += 1

    return instances


def autoScale(ins, A):
    i, n, ans = 0, len(A), ins
    while i < n:
        # print(f'{i}-th second, utility is {A[i]}, instance number before action is {ans}')
        if A[i] < 25 and ans > 1:
            ans, i = (ans + 1) // 2, i + 10
        elif A[i] > 60 and ans <= int(1e8):
            ans, i = ans * 2, i + 10
        i += 1
    return ans


# ins, A = 1, [5, 10, 80]
# print(autoScale(ins, A))
#
# ins, A = 2, [25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80]
# print(autoScale(ins, A))

print(autoScale(5, [30, 5, 4, 8, 19, 89]))
