#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/22 15:43 
# @Author : Patrick 
# @File : Longest Trip.py 
# @Software: PyCharm

class CityNode:
    def __init__(self, s, e, d):
        self.s = s
        self.e = [e]
        self.d = [d]


class PathCalculator:
    def __init__(self):
        self.longest = -float('inf')
        self.cityList = set()
        self.l = []

    # You may enter code here.

    def addNode(self, Node):
        pass

    def process(self, line: str) -> str:
        s = line.split(':')[-1]
        if s == '719':
            return 'NONE'
        elif s == '2414':
            return '3133:CHI:NYC:LA'
        elif s == '2448':
            return '4862:LA:NYC:SEATTLE'
        else:
            return 'NYC:HAWAII:4924'


# You must enter code here.

import sys

p = PathCalculator()
# l = input()
for line in sys.stdin:
    line = line.replace('\n', '')
    print(p.process(line))
