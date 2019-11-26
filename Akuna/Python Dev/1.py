#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/22 14:52 
# @Author : Patrick 
# @File : Genre.py 
# @Software: PyCharm


def process(line: str) -> str:
    # Return 'VALID' or 'INVALID'

    import string
    if not all(c in string.hexdigits for c in line):
        return 'INVALID'
    temp = int(line[2:], 16)

    s = sum(list(map(int, list(str(temp)))))

    dexTohex = hex(s).split('x')[-1]
    if dexTohex != line[:2].lower():
        return 'INVALID'
    else:
        return 'VALID'


print(process('00000000'))
