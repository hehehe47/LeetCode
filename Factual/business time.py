#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/15 16:24 
# @Author : Patrick 
# @File : business time.py
# @Software: PyCharm

import json


def sol(businesses):
    business_count = 0
    for bus in businesses:
        j = json.load(bus)
        if 'sunday' in j['hours']:
            time = j['hours']['sunday']
            if int(time.split(':')[0]) < 10:
                business_count += 1
    return business_count
