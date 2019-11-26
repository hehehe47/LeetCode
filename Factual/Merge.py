#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/15 16:43 
# @Author : Patrick 
# @File : Merge.py 
# @Software: PyCharm


def solution(inputTable):
    dc = {}
    mlen = 0
    for i in inputTable:
        if i[1] not in dc:
            dc[i[1]] = [i[0]]
        else:
            dc[i[1]].append(i[0])
    for k, v in dc.items():
        if len(v) > mlen:
            mlen = len(v)
            mkey = k
    for k, v in dc.items():
        if len(v) != mlen:
            tmp = [i for i in dc[mkey] if i not in v]
            for i in tmp:
                inputTable.append([i, k, 0])

    import numpy as np
    import pandas as pd
    table = pd.DataFrame(inputTable, columns=['City', 'Category', 'Count'])
    table[['Count']] = table[['Count']].astype(int)

    g = table.groupby(['City', 'Category']).agg({'Count': [np.sum]})

    a = g[g.columns[-1]].values
    b = np.reshape(a, (2, -1))
    return b


print(solution([
    ["Boston", "Seafood", "194"],
    ["Boston", "Mexican", "163"],
    ["Los Angeles", "Mexican", "1389"],
    ["Los Angeles", "American", "1239"],
    ["Los Angeles", "Seafood", "456"]
]))
