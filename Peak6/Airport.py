#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/18 17:04 
# @Author : Patrick 
# @File : Airport.py 
# @Software: PyCharm


def getMinGates(landingTimes, takeOffTimes, maxWaitTime, initalPlanes):
    ans, av = 0, 0
    llt = len(landingTimes)
    lwt = [i + maxWaitTime if (i + maxWaitTime) % 100 < 60 else ((i // 100 + 1) * 100 + (i + maxWaitTime) % 100 - 60)
           for
           i in landingTimes]
    i, j = 0, 0
    while i < llt:
        if lwt[i] < takeOffTimes[j]:
            if av == 0:
                ans += 1
            else:
                av -= 1
            i += 1
        else:
            av += 1
            j += 1

    a = '123'

    return initalPlanes + ans


# print(getMinGates([630, 645, 730, 1100], [700, 845, 1015, 1130], 20, 1))
print(getMinGates([340, 1240, 1250, 1600, 1715, 1832, 2204], [1144, 1305, 1318, 1544, 1612, 1801, 2141], 0, 1))
