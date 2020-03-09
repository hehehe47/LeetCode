#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/3/8 15:36 
# @Author : Patrick 
# @File : 659. Split Array into Consecutive Subsequences.py 
# @Software: PyCharm

import collections


class Solution:
    def subtract(self, i, j, d, l):
        for k in range(i, j + 1):
            d[l[k]] -= 1

    def findnext(self, d):
        for idx, (k, v) in enumerate(d.items()):
            if v != 0:
                return idx

    def isPossible(self, nums):
        left = collections.Counter(nums)
        end = collections.Counter()
        for i in nums:
            if not left[i]: continue
            left[i] -= 1
            if end[i - 1] > 0:
                end[i - 1] -= 1
                end[i] += 1
            elif left[i + 1] and left[i + 2]:
                left[i + 1] -= 1
                left[i + 2] -= 1
                end[i + 2] += 1
            else:
                return False
        return True


s = Solution()
# print(s.isPossible([1, 2, 3, 3, 4, 5]))
# print(s.isPossible([1, 2, 3, 3, 4, 4, 5, 5]))
# print(s.isPossible([1, 2, 3, 4, 4, 5]))
print(s.isPossible([1, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7, 8]))
print(s.isPossible([1, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
