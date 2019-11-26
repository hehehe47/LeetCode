#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/22 16:23 
# @Author : Patrick 
# @File : Travel Distance.py 
# @Software: PyCharm


from math import acos, sin, cos, radians, floor

RADIUS_MILES = 3963


class City:
    def __init__(self, long, lati):
        self.long = long
        self.lati = lati


class DestinationCalculator:
    def __init__(self):
        self.cityList = {}

    def calculate(self, long1, long2, lati1, lati2):
        absdifference = abs(long1 - long2)
        angle = acos(sin(lati1) * sin(lati2) + cos(lati1) * cos(lati2) * cos(absdifference))

        return angle * RADIUS_MILES

    def process(self, line: str) -> str:
        flag, p1, p2, p3 = line.split(':')
        if flag == 'LOC':
            self.cityList[p1] = City(radians(float(p3)), radians(float(p2)))
            return p1
        else:
            return p1 + ':' + p2 + ':' + p3 + ':' + str(floor(
                self.calculate(self.cityList[p2].long, self.cityList[p3].long, self.cityList[p2].lati,
                               self.cityList[p3].lati)))


import sys

p = DestinationCalculator()
p2 = DestinationCalculator()
# l = input()
for line in sys.stdin:
    line = line.replace('\n', '')
    print(p.process(line))

# LOC:CHI:41.836944:-87.684722
# LOC:NYC:40.7127:-74.0059
# TRIP:COFFEE1C:CHI:NYC
