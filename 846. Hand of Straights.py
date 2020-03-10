#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/3/9 11:56 
# @Author : Patrick 
# @File : 846. Hand of Straights.py 
# @Software: PyCharm
import collections


class Solution:
    # def isNStraightHand(self, hand, W) -> bool:
    #     if len(hand) % W != 0:
    #         return False
    #     hand = sorted(hand)
    #     d = collections.Counter(hand)
    #     d2 = collections.Counter()
    #     for i in hand:
    #         if not d[i]:
    #             continue
    #         else:
    #             for j in range(W):
    #                 if d[i + j]:
    #                     d[i + j] -= 1
    #                 else:
    #                     return False
    #     return True
    def isNStraightHand(self, hand, W):
        c = collections.Counter(hand)
        start = collections.deque()
        last_checked, opened = -1, 0
        for i in sorted(c):
            if opened > c[i] or opened > 0 and i > last_checked + 1: return False
            start.append(c[i] - opened)
            last_checked, opened = i, c[i]
            if len(start) == W: opened -= start.popleft()
        return opened == 0


s = Solution()
# print(s.isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], W=3))
# print(s.isNStraightHand(hand=[1], W=1))
print(s.isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7], W=3))
print(s.isNStraightHand(hand=[1, 2, 3, 4, 5], W=4))
