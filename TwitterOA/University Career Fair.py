#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/8 20:10 
# @Author : Patrick 
# @File : University Career Fair.py 
# @Software: PyCharm


def maxEvents(arrival, duration):
    if not arrival or not duration:
        return 0
    if len(arrival) == 1:
        return 1
    arr_dur = sorted(list(zip(arrival, duration)),
                     key=lambda p: (sum(p), p[1]))
    ans, end = 0, -float('inf')
    for arr, dur in arr_dur:
        if arr >= end:
            ans, end = ans + 1, arr + dur
    return ans

    # count = 0
    # end = [arrival[i] + duration[i] for i in range(len(arrival))]
    # # i = 0
    # # while i < len(arrival) - 1:
    # #     j = i + 1
    # #     while arrival[i] == arrival[j]:
    # #         j += 1
    # #     if j != i + 1:
    # #         tmp = end[i:j]
    # #         fastest = min(tmp)
    # #
    # #     else:
    # #         fastest = end[i]
    # #     count += 1
    # #     i = findnext(arrival, fastest, j)
    # #     count += 1
    # i = 0
    # j = i + 1
    # while j < len(arrival):
    #     min_val = end[i]
    #     while arrival[i] == arrival[j]:
    #         if end[j] < min_val:
    #             min_val = end[j]
    #         j += 1
    #     while j<len(arrival) and arrival[j]< min_val:
    #         j += 1
    #     i = j
    #     count += 1
    #     j += 1


print(maxEvents([1, 3, 3, 5, 7], [2, 2, 1, 2, 1]))  # 4
print(maxEvents([1, 1, 1, 1, 4], [10, 3, 6, 4, 2]))  # 2
print(maxEvents([1, 1, 1, 1, 4], [1, 3, 6, 4, 200]))  # 2
print(maxEvents([1, 3, 5], [2, 20, 2]))  # 2
print(maxEvents([1], [5]))  # 1
