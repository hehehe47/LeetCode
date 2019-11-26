# !/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2019/11/6 16:30 
# @Author : Patrick 
# @File : Two sum.py 
# @Software: PyCharm


def countPairs(numCount, ratingValues, target):
    # WRITE YOUR CODE HERE
    if numCount == 0:
        return 0
    d = {}
    s = set()
    count = 0
    for num in ratingValues:
        if num in d and target - num not in s:
            count += 1
            s.add(num)
            s.add(target - num)
        else:
            d[target - num] = num
    return count


print(countPairs(8, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7))
print(countPairs(6, [8, 7, 6, 5, 4, 3, 2, 1], 6))
