#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/8 16:26 
# @Author : Patrick 
# @File : Buying Show Tickets.py 
# @Software: PyCharm

def waitingTime(tickets, p):
    # count = 0
    # i = 0
    # while tickets[p] != 0:
    #     if tickets[i] != 0:
    #         tickets[i] -= 1
    #         count += 1
    #     i += 1
    #     if i == len(tickets):
    #         i = 0
    # return count

    # method 2
    count = 0

    for i in range(len(tickets)):
        if i <= p:
            if tickets[i] < tickets[p]:
                count += tickets[i]
            else:
                count += tickets[p]
        else:
            if tickets[i] < tickets[p]:
                count += tickets[i]
            else:
                count += tickets[p] - 1
    return count


print(waitingTime([2, 6, 3, 4, 5], 2))  # 12
print(waitingTime([1, 1, 1, 1], 0))  # 1
print(waitingTime([5, 5, 2, 3], 3))  # 11
print(waitingTime([0], 0))
