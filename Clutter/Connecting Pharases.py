#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/10 16:14 
# @Author : Patrick 
# @File : Connecting Pharases.py 
# @Software: PyCharm


def generate_phrases(phrases):
    # Write your code here
    ans = []
    dtail, dhead = {}, {}
    for idx, ph in enumerate(phrases):
        head = ph.split()[0]
        tail = ph.split()[-1]
        if tail in dtail:
            dtail[tail].append(idx)
        else:
            dtail[tail] = [idx]
        if head in dhead:
            dhead[head].append(idx)
        else:
            dhead[head] = [idx]

    for k in dhead.keys():
        if dtail.get(k, None):
            for idx_tail in dtail.get(k):
                for idx_head in dhead.get(k):
                    ans.append(phrases[idx_tail] + ' ' + ' '.join(phrases[idx_head].split()[1:]))
    return ans


print(generate_phrases(['mission statement',
                        'a quick bite to eat',
                        'a chip off the old block',
                        'chocolate bar',
                        'mission impossible',
                        'a man on a mission',
                        'block party',
                        'eat my words',
                        'bar of soap']))

print(generate_phrases(['writing code',
                        'code rocks',
                        'code rocks']))
print(generate_phrases(['a',
                        'b', 'a']))
