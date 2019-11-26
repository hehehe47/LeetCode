#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/14 21:42 
# @Author : Patrick 
# @File : ip address valid.py 
# @Software: PyCharm

import re


def vaild(address):
    ans = []
    for i in address:
        if re.search(
                r'^([a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4})$',
                i):
            ans.append('IPv6')
        elif re.search(
                r'^(([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])$',
                i):
            ans.append('IPv4')
        else:
            ans.append('Neither')
    return ans


a = '\n'.join(vaild(['121.18.19.20',
                     '0.12.12.34',
                     '::1'  # IPv6
                     ]))
print(a)
